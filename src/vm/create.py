```python
from pyVim.connect import SmartConnectNoSSL, Disconnect
from pyVmomi import vim
import ssl
from rich.console import Console

console = Console()

def create_vm(vcenter_host, vcenter_user, vcenter_password, datacenter_name, cluster_name, vm_name, template_name):
    try:
        # Disable SSL certificate verification (not recommended for production)
        context = ssl._create_unverified_context()
        
        # Connect to the vCenter
        si = SmartConnectNoSSL(host=vcenter_host, user=vcenter_user, pwd=vcenter_password, sslContext=context)
        content = si.RetrieveContent()

        # Find the datacenter
        datacenter = None
        for dc in content.rootFolder.childEntity:
            if dc.name == datacenter_name:
                datacenter = dc
                break

        if not datacenter:
            console.print(f"Datacenter '{datacenter_name}' not found.", style="red")
            return

        # Find the cluster
        cluster = None
        for host_folder in datacenter.hostFolder.childEntity:
            for compute_resource in host_folder.childEntity:
                if compute_resource.name == cluster_name:
                    cluster = compute_resource
                    break

        if not cluster:
            console.print(f"Cluster '{cluster_name}' not found.", style="red")
            return

        # Find the template
        template_vm = None
        for vm in datacenter.vmFolder.childEntity:
            if vm.name == template_name and isinstance(vm, vim.VirtualMachine):
                template_vm = vm
                break

        if not template_vm:
            console.print(f"Template '{template_name}' not found.", style="red")
            return

        # Clone the VM from the template
        relocate_spec = vim.vm.RelocateSpec()
        relocate_spec.pool = cluster.resourcePool

        clone_spec = vim.vm.CloneSpec()
        clone_spec.location = relocate_spec
        clone_spec.powerOn = False

        task = template_vm.Clone(folder=datacenter.vmFolder, name=vm_name, spec=clone_spec)
        
        # Wait for the task to complete
        while task.info.state == vim.TaskInfo.State.running or task.info.state == vim.TaskInfo.State.queued:
            console.print("VM creation in progress...", style="yellow")
            time.sleep(5)

        if task.info.state == vim.TaskInfo.State.success:
            console.print(f"VM '{vm_name}' created successfully.", style="green")
            vm = task.info.result
            console.print(f"VM Summary: Name - {vm.name}, CPU - {vm.config.hardware.numCPU}, Memory - {vm.config.hardware.memoryMB} MB", style="blue")
        else:
            console.print(f"Failed to create VM '{vm_name}'. Error: {task.info.error}", style="red")

    except Exception as e:
        console.print(f"An error occurred: {str(e)}", style="red")

    finally:
        Disconnect(si)

# Example CLI usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Create a VM from a template on VMware VCF')
    parser.add_argument('--vcenter-host', required=True, help='vCenter Host')
    parser.add_argument('--vcenter-user', required=True, help='vCenter User')
    parser.add_argument('--vcenter-password', required=True, help='vCenter Password')
    parser.add_argument('--datacenter-name', required=True, help='Datacenter Name')
    parser.add_argument('--cluster-name', required=True, help='Cluster Name')
    parser.add_argument('--vm-name', required=True, help='VM Name')
    parser.add_argument('--template-name', required=True, help='Template Name')

    args = parser.parse_args()

    create_vm(
        vcenter_host=args.vcenter_host,
        vcenter_user=args.vcenter_user,
        vcenter_password=args.vcenter_password,
        datacenter_name=args.datacenter_name,
        cluster_name=args.cluster_name,
        vm_name=args.vm_name,
        template_name=args.template_name
    )
```
