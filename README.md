```markdown
# VM Creation Module

This module provides functionality to create a virtual machine in a VMware VCF environment using the vSphere API (pyvmomi).

## Usage

To use this module, you need to have the `pyvmomi` library installed. You can install it via pip:

```bash
pip install pyvmomi
```

### CLI Command

The module exposes a command-line interface to create VMs. Here is an example of how to use it:

```bash
python main.py create --vcenter-host <vcenter_host> --vcenter-user <vcenter_user> --vcenter-password <vcenter_password> \
                     --vm-name <vm_name> --datacenter-name <datacenter_name> --cluster-name <cluster_name> \
                     --template-name <template_name>
```

### Parameters

- `--vcenter-host`: The hostname or IP address of the vCenter server.
- `--vcenter-user`: The username for vCenter authentication.
- `--vcenter-password`: The password for vCenter authentication.
- `--vm-name`: The name of the VM to create.
- `--datacenter-name`: The name of the datacenter where the VM will be created.
- `--cluster-name`: The name of the cluster within the datacenter where the VM will be created.
- `--template-name`: The name of the template from which the VM will be cloned.

## Error Handling

The module includes error handling for common issues such as:

- Duplicate VM names
- Invalid arguments
- Unspecified errors

Each error case is accompanied by a clear message to help users understand what went wrong.
```
