from airflow.sdk import dag, task

@dag(
    dag_id='versioned_dag',
)

def versioned_dag():

    @task.python
    def first_task():
        print("This is the First dag")

    @task.python
    def second_task():
        print("This is the Second dag")

    @task.python
    def third_task():
        print("This is the Third dag")

    @task.python
    def version_task():
        print("This is the version task, dag version 2.0!")

    first = first_task()
    second = second_task()
    third = third_task()
    version = version_task()

    first >> second >> third >> version 

versioned_dag()