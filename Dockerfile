FROM bitnami/spark:3.5

USER root
WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=$PYTHONPATH:/app

# Default command to run the ETL job
ENTRYPOINT ["spark-submit", "src/main.py"]