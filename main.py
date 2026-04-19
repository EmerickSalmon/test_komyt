```python
import argparse
from src.vm import create

def main():
    parser = argparse.ArgumentParser(description="Create a VM in VMware VCF environment.")
    parser.add_argument("name", help="Name of the VM")
    # Add other required and optional arguments here

    args = parser.parse_args()

    try:
        create.create_vm(args.name, **vars(args))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
