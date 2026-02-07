from pyspark.sql import SparkSession
import os

def get_spark_session(app_name: str = "ETLJob"):
    """Initializes a Spark Session."""
    return SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()

def read_csv(spark: SparkSession, path: str):
    """Reads a CSV file with schema inference."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found at {path}")
    return spark.read.csv(path, header=True, inferSchema=True)

def write_parquet(df, path: str, partition_by: str = None):
    """Writes a DataFrame to Parquet format."""
    writer = df.write.mode("overwrite")
    if partition_by:
        writer = writer.partitionBy(partition_by)
    writer.parquet(path)
