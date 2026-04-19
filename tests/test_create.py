```python
import unittest
from src.vm.create import create_vm

class TestCreateVM(unittest.TestCase):
    def test_valid_parameters(self):
        params = {
            "name": "vm1",
            "memory_mb": 4096,
            "num_cpus": 2,
            "disk_gb": 50
        }
        self.assertTrue(create_vm(params))

    def test_invalid_memory_type(self):
        params = {
            "name": "vm1",
            "memory_mb": "four GB",  # Invalid type
            "num_cpus": 2,
            "disk_gb": 50
        }
        with self.assertRaises(ValueError):
            create_vm(params)

    def test_invalid_cpu_count(self):
        params = {
            "name": "vm1",
            "memory_mb": 4096,
            "num_cpus": -1,  # Invalid value
            "disk_gb": 50
        }
        with self.assertRaises(ValueError):
            create_vm(params)

    def test_missing_parameter(self):
        params = {
            "name": "vm1",
            "memory_mb": 4096,
            # Missing 'num_cpus' and 'disk_gb'
        }
        with self.assertRaises(KeyError):
            create_vm(params)

if __name__ == "__main__":
    unittest.main()
```
