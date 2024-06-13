from declara_etl import DeclaraETL, LocalDriver, Task

env_var = dict(
    dataset_name = "Iris"
)

with DeclaraETL(driver=LocalDriver, env_var=env_var):

    file = "examples/quick_start/sample.yml"
    task = Task(open(file, 'r').read())
    task.run()
