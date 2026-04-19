```python
def create_vm(name, template_name, cluster, datastore, num_cpus, memory_mb):
    if not name or not template_name or not cluster or not datastore:
        raise ValueError("Name, Template Name, Cluster, and Datastore are required.")

    if not isinstance(num_cpus, int) or not isinstance(memory_mb, int):
        raise TypeError("Number of CPUs and Memory (MB) must be integers.")

    if num_cpus <= 0 or memory_mb <= 0:
        raise ValueError("Number of CPUs and Memory (MB) must be greater than zero.")
```
