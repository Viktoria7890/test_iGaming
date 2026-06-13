from apscheduler.schedulers.background import (
    BackgroundScheduler
)

from app.workers.retry_worker import (
    RetryWorker
)


scheduler = (
    BackgroundScheduler()
)


def start_scheduler():

    worker = RetryWorker()

    scheduler.add_job(
        worker.run,
        "interval",
        seconds=30
    )

    scheduler.start()