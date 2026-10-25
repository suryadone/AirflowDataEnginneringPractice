from airflow.sdk import dag, task
from pendulum import datetime
from airflow.timetables.events import EventsTimetable

special_dates = EventsTimetable(
    event_dates=[
        datetime(2026,10,1),
        datetime(2026,10,11),
        datetime(2026,10,17),
        datetime(2026,10,21)
    ]
)

@dag(
    schedule = special_dates,
    start_date=datetime(year=2026, month=10, day=14,tz="America/Halifax"),
    end_date=datetime(year=2026, month=10, day=24,tz="America/Halifax"),
    catchup=True
)

def special_dates_dag():

    @task.python
    def special_event_task(**kwargs):
        execution_date =kwargs['logical_date']
        print(f"Running task from special events on {execution_date}")

    special_event = special_event_task()

special_dates_dag()