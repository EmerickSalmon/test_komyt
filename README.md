# VM Creation Module Documentation

This module allows users to create virtual machines on a VMware VCF environment using the vSphere API (pyvmomi). The user can specify the VM parameters via the command line interface (CLI).

## Usage

### Interactive Input
Run the `create` command without any parameters, and you will be prompted to enter the required details interactively.

```sh
python -m src.vm.create
```

### Direct Parameter Specification
You can also specify all parameters directly in the command line. Here is an example:

```sh
python -m src.vm.create --name "my-vm" --datastore "DS1" --network "VM Network" --memory 4096 --cpus 2
```

### Supported Parameters

- `--name`: Name of the virtual machine (required)
- `--datastore`: Datastore where the VM will be created (required)
- `--network`: Network to which the VM will connect (required)
- `--memory`: Amount of memory in MB (default: 2048)
- `--cpus`: Number of CPUs (default: 1)
- `--template`: Template name for cloning (optional)

### Error Handling
Errors are handled gracefully, and explicit messages are provided to the user. For example:

- If a required parameter is missing, the user will be informed which parameter is needed.
- If there is an issue with the vCenter connection or API interaction, appropriate error messages will be displayed.

## Testing

To ensure that the `create` command works correctly, you can run the following commands:

1. **Linting**: Check for syntax and style errors.
    ```sh
    flake8
    ```

2. **Unit Tests**: Run the unit tests to validate parameter validation.
    ```sh
    python -m unittest discover
    ```

## Verification

Before finishing, run these commands inside the container to verify that everything is working correctly:

- Linting:
    ```sh
    flake8
    ```

- Unit Tests:
    ```sh
    python -m unittest discover
    ```

Ensure all commands exit with status 0 before marking this task as complete.

