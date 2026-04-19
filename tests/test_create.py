```python
import unittest
from src.vm.create import create_vm

class TestCreateVM(unittest.TestCase):
    def test_create_vm(self):
        self.assertTrue(callable(create_vm))
```
