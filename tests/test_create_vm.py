```python
import unittest
from unittest.mock import patch
from src.vm.create import create_vm

class TestCreateVM(unittest.TestCase):

    @patch('src.vm.create.create_vm')
    def test_param_validation(self, mock_create_vm):
        # Mock the function to prevent actual API calls
        mock_create_vm.return_value = None

        # Example parameters for testing
        params = {
            'name': 'test-vm',
            'memory': 4096,
            'cpus': 2,
            'template_name': 'base-template'
        }

        try:
            create_vm(params)
            self.assertTrue(mock_create_vm.called)
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def test_invalid_memory(self):
        with self.assertRaises(ValueError) as context:
            create_vm({'memory': -1, 'cpus': 2, 'name': 'test-vm', 'template_name': 'base-template'})
        self.assertEqual(str(context.exception), "Memory must be a positive integer.")

    def test_invalid_cpus(self):
        with self.assertRaises(ValueError) as context:
            create_vm({'memory': 4096, 'cpus': -1, 'name': 'test-vm', 'template_name': 'base-template'})
        self.assertEqual(str(context.exception), "CPUs must be a positive integer.")

    def test_missing_name(self):
        with self.assertRaises(KeyError) as context:
            create_vm({'memory': 4096, 'cpus': 2, 'template_name': 'base-template'})
        self.assertEqual(str(context.exception), "'name'")

    def test_missing_template_name(self):
        with self.assertRaises(KeyError) as context:
            create_vm({'memory': 4096, 'cpus': 2, 'name': 'test-vm'})
        self.assertEqual(str(context.exception), "'template_name'")
```
