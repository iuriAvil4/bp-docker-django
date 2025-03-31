from django.urls import path
from a_home.views import testando_funcao

urlpatterns = [
    path('teste/', testando_funcao, name='testando_funcao')
]
