# Big Data ETL Engine

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Spark](https://img.shields.io/badge/Apache_Spark-3.5-orange.svg)](https://spark.apache.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade ETL (Extract, Transform, Load) engine** for big data processing. Built with PySpark, this platform provides a scalable and robust framework for ingesting raw data, applying complex transformations, and exporting optimized datasets.

## 🚀 Features

- **Scalable Ingestion**: Handles large-scale CSV, JSON, and Parquet data sources.
- **Advanced Transformations**: Distributed data cleaning, normalization, and complex aggregations.
- **Optimized Storage**: Exports results to Parquet with appropriate partitioning for high-performance querying.
- **Schema Enforcement**: Ensures data quality with strict schema verification.
- **Modular Pipeline**: Decoupled IO, transformation, and validation logic.
- **Containerized**: Full Spark cluster setup via Docker Compose for local development and testing.

## 📁 Project Structure

```
data-big-data-etl-engine/
├── src/
│   ├── transformations/ # Data processing logic
│   ├── utils/           # Spark session and IO helpers
│   └── main.py          # Job entrypoint
├── data/                # Sample input datasets
├── tests/               # PySpark unit tests
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/data-big-data-etl-engine.git

# Run with Docker Compose
docker-compose up --build
```

## 📄 License

MIT License
