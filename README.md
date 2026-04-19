# VM Management CLI

## Commands

### Create
Create a virtual machine.

```sh
python main.py create --name <vm_name> --template <template_name> --datastore <datastore_name> --resource_pool <resource_pool_name>
```

- `--name`: Name of the VM.
- `--template`: Template to clone from.
- `--datastore`: Datastore for the VM.
- `--resource_pool`: Resource pool for the VM.
