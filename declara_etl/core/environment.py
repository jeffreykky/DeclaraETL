import os

from declara_etl.core.context import context

class Environment:

    def __init__(self, driver, env_var: dict = {}) -> None:
        self._get_env_var()
        context.env_var.update(env_var)
        context.driver = driver()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        context.setup()

    def _get_env_var(self):
        env_var = dict()
        for key, value in os.environ.items():
            if key.startswith("DECLARA_"):
                env_var[key.removeprefix("DECLARA_").lower()]=value
        context.env_var = env_var
