from celery import shared_task


def more_time_task():
    for i in range(100000):
        print(i)


@shared_task
def add():
    more_time_task()
