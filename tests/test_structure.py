import pytest
import os
from pathlib import Path

# List of expected modules that should be importable
EXPECTED_MODULES = [
    "client",
    "crud.create",
    "crud.read",
    "crud.update",
    "crud.delete",
]

def test_structure_importability():
    """
    Test that all CRUD modules are importable without raising ImportError.
    This test verifies the project structure and importability without actual vCenter connection.
    """
    for module in EXPECTED_MODULES:
        module_path = Path(module).with_suffix(".py")
        if not module_path.exists():
            pytest.fail(f"Missing module file: {module_path}")

        # Attempt to import the module
        try:
            __import__(module)
        except ImportError as e:
            pytest.fail(f"Failed to import {module}: {e}")

    # Verify that the main module is importable
    try:
        __import__("main")
    except ImportError as e:
        pytest.fail(f"Failed to import main module: {e}")

    # Verify that the client module is importable
    try:
        __import__("client")
    except ImportError as e:
        pytest.fail(f"Failed to import client module: {e}")

    # Verify that the requirements.txt exists
    requirements_path = Path("requirements.txt")
    if not requirements_path.exists():
        pytest.fail("requirements.txt is missing")

    # Verify that .env.example exists
    env_example_path = Path(".env.example")
    if not env_example-1000
    if not env_example_path.exists():
        pytest.fail(".env.example is missing")

    # Verify that .gitignore exists and excludes .env, __pycache__, and .pytest_cache
    gitignore_path = Path(".gitignore")
    if not gitignore_path.exists():
        pytest.fail(".gitignore is missing")

    with open(gitignore_path, 'r') as f:
        content = f.read()
        if ".env" not in content or "__pycache__" not in content or ".pytest_cache" not in content:
            pytest.fail("Missing required entries in .gitignore")
