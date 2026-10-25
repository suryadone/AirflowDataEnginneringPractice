from airflow.sdk import dag, task
from pendulum import datetime,duration
from airflow.timetables.trigger import DeltaTriggerTimetable

@dag(
    dag_id = 'delta_schedule_dag',
    start_date= datetime(year=2026, month=10, day=14, tz='America/Halifax'),
    schedule = DeltaTriggerTimetable(duration(days=3)),
    end_date= datetime(year=2026, month=10, day=24, tz='America/Halifax'),
    is_paused_upon_creation=False,
    catchup=True
)

def delta_schedule_dag():

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

delta_schedule_dag() 