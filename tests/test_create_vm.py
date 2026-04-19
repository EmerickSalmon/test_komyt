```python
import unittest
from src.vm.create import create_vm

class TestCreateVM(unittest.TestCase):
    def test_parameter_validation(self):
        with self.assertRaises(ValueError) as context:
            create_vm(None, None, None, None, None, None, None)
        self.assertIn("Argument", str(context.exception))

if __name__ == '__main__':
    unittest.main()
```
