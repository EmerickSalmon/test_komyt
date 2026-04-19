# VM Creation Module

This module allows you to create a virtual machine on a VMware VCF environment using the vSphere API.

## Usage

To create a VM, use the following command:

```bash
python main.py <host> <user> <password> <vm_name> <datastore_name> <template_name> [--num_cpus <num_cpus>] [--memory_mb <memory_mb>]
```

- `<host>`: vCenter host address.
- `<user>`: vCenter username.
- `<password>`: vCenter password.
- `<vm_name>`: Name of the VM to create.
- `<datastore_name>`: Datastore where the VM will be created.
- `<template_name>`: Template VM name to clone from.
- `--num_cpus`: Number of CPUs for the VM (default is 1).
- `--memory_mb`: Memory (in MB) for the VM (default is 512).

## Error Handling

The module includes error handling for common issues such as:
- Duplicate VM names.
- Insufficient resources.
- Missing datastores or templates.

## Testing and Linting

To run tests, use:

```bash
python -m unittest discover
```

To lint the code, use:

```bash
flake8
```
