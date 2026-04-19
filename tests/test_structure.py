import unittest
import os

class TestStructure(unittest.TestCase):
    def test_file_structure(self):
        expected_files = [
            'src/__init__.py',
            'src/client.py',
            'src/client/__init__.py',
            'src/client/client.py',
            'src/create.py',
            'src/create/__init__.py',
            'src/delete.py',
            'src/delete/__init__.py',
            'src/main.py',
            'src/read.py',
            'src/read/__init__.py',
            'src/update.py',
            'src/update/__init__.py',
            'src/vm/create.py',
        ]
        for file in expected_files:
            self.assertTrue(os.path.exists(file), f"File {file} does not exist")

if __name__ == '__main__':
    unittest.main()
