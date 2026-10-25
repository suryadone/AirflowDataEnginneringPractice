from airflow.sdk import dag, task

@dag(
    dag_id = 'first_dag',
)

def first_dag():

    @task.python
    def first_task():
        print("this is the First Task")

    @task.python
    def second_task():
        print("this is the Second Task")

    @task.python
    def third_task():
        print("this is the Third Task, dag is completed!")


    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third

first_dag()