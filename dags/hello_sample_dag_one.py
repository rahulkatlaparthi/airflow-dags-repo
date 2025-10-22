from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello from Airflow DAG!")

with DAG(
    'hello_sample_dag_one',
    start_date=datetime(2025, 10, 20),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = PythonOperator(
        task_id='say_hello',
        python_callable=hello
    )
