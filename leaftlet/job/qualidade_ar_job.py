from leaftlet.service.qualidade_ar import listar_todos
from apscheduler.schedulers.background import BackgroundScheduler
from leaftlet.integrations import cetesb

_consulta = cetesb.Consulta(True)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(_consulta.principal, 'interval', minutes=60)
    scheduler.add_job(_consulta.detalhes, 'interval', minutes=60)
    scheduler.start()
