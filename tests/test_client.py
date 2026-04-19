import pytest
from client import VCenterClient

def test_vcenter_client_import_and_init():
    """
    Test that VCenterClient can be imported and instantiated without raising an exception.
    This test does not require an actual vCenter connection.
    """
    # Verify that VCenterClient is importable
    try:
        from client import VCenterClient
    except ImportError as e:
        pytest.fail(f"Failed to import VCenterClient: {e}")

    # Test that the constructor can be called without raising an exception
    try:
        client = VCenterClient(
            host="localhost",
            user="admin",
            password="password",
            port=443
        )
    except Exception as e:
        pytest.fail(f"VCenterClient constructor raised an exception: {e}")

    # Optional: Verify that the instance has expected attributes
    assert hasattr(client, "host"), "VCenterClient instance missing 'host' attribute"
    assert hasattr(client, "user"), "VCenterClient instance missing 'user' attribute"
    assert hasattr(client, "password"), "VCenterClient instance missing 'password' attribute"
    assert hasattr(client, "port"), "VCenterClient instance missing 'port' attribute"
