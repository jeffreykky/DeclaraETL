# DeclaraETL

DeclaraETL is a Python library for building Spark data pipelines using task configurations defined in YAML format. The library simplifies the process of configuring and running Spark jobs, making it easier to manage complex data workflows.

## Features

- Define Spark data pipeline tasks in YAML configuration files
- Automatically handle the execution of tasks based on the YAML configuration
- Support for both local Spark environment and AWS Glue Spark Shell

## Installation

To install DeclaraETL, use pip:
```sh
pip install declara_etl
```


## Running the Pipeline
```py
from declara_etl import DeclaraETL, LocalDriver, Task

env_var = dict(
    dataset_name = "Iris"
)

with DeclaraETL(driver=LocalDriver, env_var=env_var):

    file = "examples/quick_start/sample.yml"
    task = Task(open(file, 'r').read())
    task.run()

```

## TODO

Pending items and features:

- [ ] Logging
  - Implement comprehensive logging for all operations
  - Support for different logging levels (INFO, DEBUG, ERROR)

- [ ] Spark Session Reset
  - Implement functionality to reset or recreate Spark sessions as needed
  - Ensure it supports complex, long, iterative pipelines

- [ ] Task Level Variable Control
  - Add support for defining and using variables at the task level
  - Ensure variables can be referenced within task configurations

- [ ] Environment Level Variable Control
  - Implement support for environment-specific variables
  - Allow for easy switching between different environments (e.g., development, staging, production)

- [ ] Additional Operators
  - Implement additional operators for different data sources and sinks
  - Support for more complex data transformations
  - e.g BranchOperator