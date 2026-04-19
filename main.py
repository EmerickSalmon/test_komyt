```python
import argparse
from src.vm.create import create_vm

def main():
    parser = argparse.ArgumentParser(description="CLI to manage VMware VMs")
    subparsers = parser.add_subparsers(dest='command')

    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new VM')
    create_parser.add_argument('--name', type=str, help='Name of the VM')
    create_parser.add_argument('--template', type=str, help='Template to clone from')
    create_parser.add_argument('--datastore', type=str, help='Datastore to place the VM')
    create_parser.add_argument('--network', type=str, help='Network for the VM')

    args = parser.parse_args()

    if args.command == 'create':
        try:
            create_vm(args)
        except Exception as e:
            print(f"Error creating VM: {e}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```
