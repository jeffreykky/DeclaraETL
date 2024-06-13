from pyspark.sql import SparkSession

from declara_etl.types.driver import DriverT

class LocalDriver(DriverT):


    def __init__(self):
        super().__init__()
        self.spark = SparkSession\
            .builder\
            .config('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.3.4,org.apache.hadoop:hadoop-common:3.3.4')\
            .getOrCreate()