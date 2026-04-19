```python
import argparse
from src.create import create_vm

def main():
    parser = argparse.ArgumentParser(description="VM Management Tool")
    subparsers = parser.add_subparsers(dest='command')

    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new virtual machine')
    create_parser.add_argument('--name', type=str, required=True, help='Name of the VM')
    create_parser.add_argument('--template', type=str, required=True, help='Template to clone from')
    create_parser.add_argument('--datacenter', type=str, required=True, help='Datacenter name')
    create_parser.add_argument('--cluster', type=str, required=True, help='Cluster name')
    create_parser.add_argument('--resource_pool', type=str, required=True, help='Resource pool name')

    args = parser.parse_args()

    if args.command == 'create':
        create_vm(args.name, args.template, args.datacenter, args.cluster, args.resource_pool)

if __name__ == "__main__":
    main()
```
