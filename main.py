```python

import argparse
from rich.console import Console

console = Console()

def parse_arguments():
    parser = argparse.ArgumentParser(description="VM Creation Tool")
    subparsers = parser.add_subparsers(dest='command')
    
    create_parser = subparsers.add_parser('create', help='Create a new VM')
    create_parser.add_argument('--name', required=True, help='Name of the VM')
    create_parser.add_argument('--template', required=True, help='Template to clone from')
    create_parser.add_argument('--ip', required=True, help='IP address for the VM')
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    if args.command == 'create':
        try:
            from src.vm.create import create_vm
            vm_info = create_vm(args.name, args.template, args.ip)
            console.print(f"VM Created Successfully:\nName: {vm_info['name']}\nUUID: {vm_info['uuid']}\nIP Address: {vm_info['ip']}\nStatus: Running", style="bold green")
        except Exception as e:
            console.print(f"Error creating VM: {str(e)}", style="bold red")

if __name__ == '__main__':
    main()
```
