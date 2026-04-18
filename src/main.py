```python
import sys
from rich.console import Console
from rich.menu import Menu
from rich.panel import Panel
from rich.prompt import Prompt

def main():
    console = Console()
    
    console.print(Panel("[bold green]VMware Cloud Foundation VM Manager[/bold green]"))
    
    menu_options = {
        "1": "create_vm",
        "2": "list_vms",
        "3": "update_vm",
        "4": "delete_vm"
    }
    
    while True:
        console.print("\n" + "-" * 50)
        console.print("Select an operation:")
        console.print("1. Create VM")
        console.print("2. List VMs")
        console.print("3. Update VM")
        console.print("4. Delete VM")
        console.print("0. Exit")
        console.print("-" * 50)
        
        choice = Prompt.ask("Enter your choice", default="0")
        
        if choice == "0":
            console.print("[bold yellow]Goodbye![/bold yellow]")
            break
        
        if choice not in menu_options:
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")
            continue
        
        operation = menu_options[choice]
        
        console.print(f"\nExecuting: [bold]{operation}[/bold]")
        
        # Simulate function call - actual implementation would be here
        if operation == "create_vm":
            print("create_vm function called (not implemented)")
        elif operation == "list_vms":
            print("list_vms function called (not implemented)")
        elif operation == "update_vm":
            print("update_vm function called (not implemented)")
        elif operation == "delete_vm":
            print("delete_vm function called (not implemented)")

if __name__ &__name__ == "__main__":
    main()
```
