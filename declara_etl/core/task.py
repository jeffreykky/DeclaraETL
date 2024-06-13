from jinja2 import Template

from declara_etl.core.context import context
from declara_etl.utils import yaml, import_operators

class Task:

    def __init__(self, task_setting, task_var:dict = dict(), **kwargs):
        task_setting = Template(task_setting).render(env=context.env_var, task=task_var)
        self.setting = yaml.load(task_setting, Loader=yaml.SafeLoader)
        self.version = self.setting["version"]
        self.pipeline = self.setting["pipeline"]
        context.operators = import_operators([])
        

    def run(self):
        jobs = []
        for job_name, config in self.pipeline.items():
            op = context.operators[config["operator"]]
            jobs.append(op(job_name=job_name, **config))
        for job in jobs:
            job.run()