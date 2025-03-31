from django.shortcuts import render, redirect
from django.http import HttpResponse

from .tasks import send_custom_email


def testando_funcao(request):
    if request.method == "POST":
        subject = "Testando"
        message = f"Testando metodo assincrono projeto docker-tutorial"
        send_custom_email.delay(subject, message, ["iuriguerra03@gmail.com"])

        return HttpResponse("Email disparado com sucesso")
    
    form_html = """
    <form method="post">
        <input type="hidden" name="csrfmiddlewaretoken" value="">
        <button type="submit">Enviar email de teste</button>
    </form>
    <script>
        document.querySelector('input[name="csrfmiddlewaretoken"]').value = 
            document.cookie.split('; ').find(row => row.startsWith('csrftoken=')).split('=')[1];
    </script>
    """
    return HttpResponse(f"Use o método POST para testar. {form_html}")