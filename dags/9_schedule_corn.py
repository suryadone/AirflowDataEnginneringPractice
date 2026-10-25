from airflow.sdk import dag, task
from pendulum import datetime
from airflow.timetables.trigger import CronTriggerTimetable

@dag(
    dag_id = 'corn_schedule_dag',
    start_date= datetime(year=2026, month=10, day=14, tz='America/Halifax'),
    schedule = CronTriggerTimetable("0 16 * * MON-FRI",timezone='America/Halifax'),
    end_date= datetime(year=2026, month=10, day=24, tz='America/Halifax'),
    is_paused_upon_creation=False,
    catchup=True
)

def corn_schedule_dag():

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

corn_schedule_dag() 