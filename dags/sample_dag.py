from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
}

def hello():
    print("Hello from Airflow DAG!")

with DAG(
    dag_id='hello_sample_dag1',
    default_args=default_args,
    start_date=datetime(2025, 10, 20),
    schedule='@daily',  # updated for Airflow 3.x
    catchup=False
) as dag:
    
    task1 = PythonOperator(
        task_id='say_hello',
        python_callable=hello
    )
