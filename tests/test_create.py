```python
import unittest
from src.create import create_vm

class TestCreateVM(unittest.TestCase):
    def test_create_vm(self):
        # Basic test to check if the function runs without errors
        create_vm(name="TestVM", template="BaseTemplate", datacenter="Datacenter1", cluster="Cluster1", resource_pool="ResourcePool1")

if __name__ == '__main__':
    unittest.main()
```
