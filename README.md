# Module create.py

This module allows for the creation of a virtual machine on a VMware VCF environment using the vSphere API (pyvmomi). Users can specify VM parameters via the command line interface.

## Usage

To use the `create.py` module, run the following command:

```bash
python create.py --param1 value1 --param2 value2 ...
```

Replace `--param1`, `--param2`, etc., with the actual parameters required for your virtual machine configuration.

## Parameters

- `--param1`: Description of parameter 1.
- `--param2`: Description of parameter 2.
- ...

For a full list of parameters, use:

```bash
python create.py --help
```

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- pyvmomi library (`pip install pyvmomi`)

## Example

Create a virtual machine with specific configurations:

```bash
python create.py --name myVM --cpu 4 --memory 8192
```

This will create a VM named "myVM" with 4 CPUs and 8GB of RAM.

