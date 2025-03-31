from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define o módulo de configurações padrão para o Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Configurações do Celery com prefixo CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descobre automaticamente tarefas em apps instalados
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
