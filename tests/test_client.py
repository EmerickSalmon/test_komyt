import unittest
from src.client.client import create_vm

class TestClient(unittest.TestCase):
    def test_create_vm(self):
        self.assertEqual(create_vm(), None)

if __name__ == '__main__':
    unittest.main()
