from django.core.mail import EmailMessage
from celery import shared_task
import time

from django.conf import settings


@shared_task(name='send_custom_email')  
def send_custom_email(subject, message, recipient_list, attachments=None):
    """
    Envia um e-mail com anexos usando as configurações do Django.
    
    :param subject: Assunto do e-mail
    :param message: Corpo do e-mail
    :param recipient_list: Lista de destinatários (ex: ['email1@email.com'])
    :param attachments: Lista de anexos [(nome_arquivo, conteudo, tipo_mime)]
    """
    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipient_list)
    
    if attachments:
        for attachment in attachments:
            filename, content, mime_type = attachment
            email.attach(filename, content, mime_type)

    email.send()
