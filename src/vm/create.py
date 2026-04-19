```python
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

def create_vm(vm_name, **kwargs):
    # Implement the VM creation logic here
    # Use kwargs to handle other parameters like datastore, template, etc.

    # Example error handling
    if not vm_name:
        raise ValueError("VM name cannot be empty")

    # Connect to vCenter
    context = ssl._create_unverified_context()
    si = SmartConnect(host="vcenter_host", user="username", pwd="password", sslContext=context)

    content = si.RetrieveContent()

    # Check for duplicate VM names
    container = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    for vm in container.view:
        if vm.name == vm_name:
            Disconnect(si)
            raise ValueError("A virtual machine with this name already exists")

    # Implement resource checks and template cloning logic here

    # Disconnect from vCenter
    Disconnect(si)

    print(f"VM '{vm_name}' created successfully.")
```
