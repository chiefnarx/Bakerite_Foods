import pandas as pd

def run_extraction():
    try:
        data = pd.read_csv("/home/chiefnarx/airflow/bakerite_foods_dag/bakerite_transaction.csv")
        print("Data loaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")