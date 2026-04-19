import unittest
from src.vm.create import create_vm

class TestCreateVM(unittest.TestCase):
    def test_validate_parameters(self):
        with self.assertRaises(Exception) as context:
            create_vm("", "template")
        self.assertIn("Name of the VM", str(context.exception))

        with self.assertRaises(Exception) as context:
            create_vm("vm_name", "")
        self.assertIn("Template name to clone from", str(context.exception))

if __name__ == '__main__':
    unittest.main()
