from airflow.sdk import dag, task
import os

@dag(
    dag_id = 'first_orchestrator_dag',
)

def first_orchestrator_dag():

    @task.python
    def first_task():
        print("this is the First Task")

    @task.python
    def second_task():
        print("this is the Second Task")

    @task.python
    def third_task():
        os.makedirs(os.path.dirname("opt/airflow/logs/data"), exist_ok=True)
        
        with open("opt/airflow/logs/data/output_1.txt", "w") as f:
            f.write(f"Data fetched Sucessfully")


    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third

first_orchestrator_dag()