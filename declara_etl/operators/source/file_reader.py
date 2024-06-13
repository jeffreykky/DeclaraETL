from declara_etl.types.operator import Reader, SparkDF

class FileReader(Reader):

    __name__ = "FileReader"

    def __init__(self, path, format, **kwargs) -> None:
        super().__init__(**kwargs)
        self.path = path
        self.format = format

    def read(self):
        df = self.spark\
                .read\
                .format(self.format)\
                .load(self.path)
        return df
    
