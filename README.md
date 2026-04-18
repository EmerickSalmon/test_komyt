# VMware Cloud Foundation (VCF) Python CRUD Tool

A Python application for performing CRUD operations on virtual machines in a VMware Cloud Foundation (VCF) environment via the vSphere API.

## Features

- Perform Create, Read, Update, and Delete (CRUD) operations on virtual machines.
- Interactive CLI menu for easy navigation.
- Modular structure with clear separation of concerns.
- Configurable via environment variables.
- Ready for future expansion with additional features.

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- vSphere client access (vCenter server)
- A valid vCenter environment with VMs to operate on

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/vcf-crud-tool.git
cd vcf-crud-tool
```

2. Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit `.env` to include your vCenter credentials and settings:

```
VCENTER_HOST=your-vcenter-host
VCENTER_USER=your-username
VCENTER_PASSWORD=your-password
VCENTER_PORT=443
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python main.py
```

The CLI will present a menu with options to:
- Create a VM
- List existing VMs
- Update a VM
- Delete a VM

## Directory Structure

```
vcf-crud-tool/
├── client.py          # vSphere client connection logic
├── main.py            # CLI menu and command routing
├── requirements.txt   # Python dependencies
├── .env.example       # Example environment variables
├── .gitignore         # Files to exclude from Git
└── tests/             # Unit tests (structure only)
```

## Testing

Run tests to verify the structure and imports:

```bash
pytest
```

Tests will pass without requiring actual vCenter connectivity.

> Note: This tool is designed for development and learning. It does not perform real operations on production environments.
