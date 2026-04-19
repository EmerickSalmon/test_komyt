# VMware VM CLI

This CLI tool allows you to manage VMware virtual machines. Currently, it supports creating new VMs from templates.

## Commands

### Create a VM

```sh
python main.py create --name <vm_name> --template <template_name> --datastore <datastore_name> --network <network_name>
```

- `--name`: The name of the VM to create.
- `--template`: The template to clone from.
- `--datastore`: The datastore where the VM will be placed.
- `--network`: The network for the VM.

If you omit any flags, you will be prompted to enter the missing values interactively.
