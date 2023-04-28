from leaftlet.service.qualidade_ar import listar_todos
from apscheduler.schedulers.background import BackgroundScheduler


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(listar_todos, 'interval', minutes=60)
    scheduler.start()
