```python
def create_vm(args):
    if not args.name:
        args.name = input("Enter the name of the VM: ")
    if not args.template:
        args.template = input("Enter the template to clone from: ")
    if not args.datastore:
        args.datastore = input("Enter the datastore for the VM: ")
    if not args.network:
        args.network = input("Enter the network for the VM: ")

    # Placeholder for actual VM creation logic
    print(f"Creating VM '{args.name}' from template '{args.template}' on datastore '{args.datastore}' with network '{args.network}'")
```
