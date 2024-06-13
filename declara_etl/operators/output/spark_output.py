from declara_etl.types.operator import Output

class SparkOutput(Output):

    __name__ = "SparkOutput"

    def __init__(self, table, format, mode, path, **kwargs) -> None:
        super().__init__(**kwargs)
        self.table = table
        self.format = format
        self.mode = mode
        self.path = path

    def output(self) -> None:
        df = self.spark.read.table(self.table)
        df.write\
            .format(self.format)\
            .mode(self.mode)\
            .save(self.path)