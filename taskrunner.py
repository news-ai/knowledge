from celery import Celery
import celeryconfig


def make_celery():
    celery = Celery(
        'taskrunner',
        broker='redis://localhost:6379/0',
        include=['articles'],
    )
    celery.config_from_object(celeryconfig)
    return celery


app = make_celery()
