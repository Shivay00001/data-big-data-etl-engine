from src.utils.io import get_spark_session, read_csv, write_parquet
from src.transformations.cleaners import clean_data, aggregate_by_category, add_processing_metadata
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_etl(input_path: str, output_path: str):
    """Main ETL job execution."""
    spark = get_spark_session("ProductionETL")
    
    try:
        logger.info(f"Reading data from {input_path}")
        df = read_csv(spark, input_path)
        
        logger.info("Starting transformations")
        df_cleaned = clean_data(df)
        df_transformed = add_processing_metadata(df_cleaned)
        
        # Example aggregation
        if "category" in df_transformed.columns and "amount" in df_transformed.columns:
            df_final = aggregate_by_category(df_transformed, "category", "amount")
        else:
            df_final = df_transformed
            
        logger.info(f"Writing results to {output_path}")
        write_parquet(df_final, output_path, partition_by="process_date")
        
        logger.info("ETL Job completed successfully")
        
    except Exception as e:
        logger.error(f"ETL Job failed: {e}")
        raise
    finally:
        spark.stop()

if __name__ == "__main__":
    import sys
    input_file = sys.argv[1] if len(sys.argv) > 1 else "data/sample.csv"
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "output/processed_data"
    run_etl(input_file, output_dir)
