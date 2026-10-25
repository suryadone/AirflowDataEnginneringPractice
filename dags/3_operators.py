from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator

@dag(
    dag_id = 'operators_dag',
)

def operators_dag():

    @task.python
    def first_task():
        print("this is the First Task")

    @task.python
    def second_task():
        print("this is the Second Task")

    @task.bash
    def bash_task_modern():
        return "echo https://airflow.apache.org/"

    bash_task_oldschool = BashOperator(
    task_id="bash_task_oldschool",
    bash_command="echo https://airflow.apache.org/",
    )


    first = first_task()
    second = second_task()
    bash_task_modern = bash_task_modern()

    first >> second >> bash_task_modern >> bash_task_oldschool

operators_dag()