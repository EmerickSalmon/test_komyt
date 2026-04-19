```python
from rich.console import Console

console = Console()

def create_vm(name, template, ip):
    # Simulate VM creation logic here
    vm_info = {
        'name': name,
        'uuid': '12345-67890',
        'ip': ip,
        'status': 'Running'
    }
    
    console.print(f"Creating VM '{name}' from template '{template}' with IP '{ip}'", style="bold yellow")
    
    # Simulate some delay
    import time
    time.sleep(2)
    
    return vm_info

# Example usage (to be removed in final implementation)
if __name__ == '__main__':
    create_vm('test-vm', 'default-template', '192.168.1.10')
```
