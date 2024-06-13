from abc import ABC, abstractmethod

from pyspark.sql.dataframe import DataFrame as SparkDF

from declara_etl.core.context import context

class Operator(ABC):

    __name__ = "Operator"

    def __init__(self, job_name, **kwargs) -> None:
        self.spark = context.driver.spark
        self.table_name = kwargs.get("table_name", job_name)

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Reader(Operator, ABC):

    __name__ = "Reader"

    @abstractmethod
    def read(self) -> SparkDF:
        raise NotImplementedError

    def run(self) -> None:
        df = self.read()
        df.createOrReplaceTempView(self.table_name)

class Transformer(Operator, ABC):

    __name__ = "Transformer"

    @abstractmethod
    def transform(self) -> SparkDF:
        raise NotImplementedError

    def run(self) -> None:
        df = self.transform()
        df.createOrReplaceTempView(self.table_name)

class Output(Operator, ABC):

    __name__ = "Output"

    @abstractmethod
    def output(self) -> None:
        raise NotImplementedError
    
    def run(self) -> None:
        self.output()

