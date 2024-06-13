

def import_operators(operator_names):
    from declara_etl.operators.source.file_reader import FileReader
    from declara_etl.operators.transform.spark_sql import SparkSQL
    from declara_etl.operators.output.spark_output import SparkOutput
    
    return dict(
        FileReader=FileReader,
        SparkSQL=SparkSQL,
        SparkOutput=SparkOutput
    )