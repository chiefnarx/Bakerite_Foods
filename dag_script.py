from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from extraction import run_extraction
from transformation import run_transformation
from loading import run_loading

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 9, 7),
    'email': 'ameereking@gmail.com',
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'bakerite_pipeline',
    default_args=default_args,
    description='This represents Bakerite Foods Data Management',
    schedule_interval=timedelta(days=1),
    catchup=False
)


extraction = PythonOperator(
    task_id = 'extraction_layer',
    python_callable = run_extraction,
    dag = dag,
)

transformation = PythonOperator(
    task_id = 'transformation_layer',
    python_callable = run_transformation,
    dag = dag,
)

loading = PythonOperator(
    task_id = 'loading_layer',
    python_callable = run_loading,
    dag = dag,
)

extraction >> transformation >> loading