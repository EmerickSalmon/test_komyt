```python
import unittest
from src.vm import create

class TestCreateVM(unittest.TestCase):
    def test_vm_creation_with_missing_name(self):
        with self.assertRaises(ValueError) as context:
            create.create_vm("")
        self.assertEqual(str(context.exception), "VM name cannot be empty")

    # Add more tests for other scenarios like duplicate names, insufficient resources, etc.

if __name__ == "__main__":
    unittest.main()
```
