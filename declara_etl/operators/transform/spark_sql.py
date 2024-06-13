from declara_etl.types.operator import Transformer

class SparkSQL(Transformer):

    __name__ = "SparkSQL"

    def __init__(self, sql, **kwargs) -> None:
        super().__init__(**kwargs)
        self.sql = sql

    def transform(self):
        df = self.spark.sql(self.sql)
        df.show(5)
        return df
