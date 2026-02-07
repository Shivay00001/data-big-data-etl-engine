from pyspark.sql import functions as F

def clean_data(df):
    """Basic data cleaning: drop nulls and trim strings."""
    return df.na.drop().select([F.trim(F.col(c)).alias(c) if t == "string" else F.col(c) for c, t in df.dtypes])

def aggregate_by_category(df, category_col: str, value_col: str):
    """Aggregates values by a specific category."""
    return df.groupBy(category_col).agg(
        F.sum(value_col).alias(f"total_{value_col}"),
        F.avg(value_col).alias(f"avg_{value_col}"),
        F.count("*").alias("count")
    )

def add_processing_metadata(df):
    """Adds processing timestamp and partition keys."""
    return df.withColumn("processed_at", F.current_timestamp()) \
             .withColumn("process_date", F.to_date(F.current_timestamp()))
