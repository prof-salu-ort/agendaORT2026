from django.urls import path

from . import views

app_name = 'agenda'

urlpatterns = [
    path('teste/', views.ola_mundo, name='ola_mundo'),
    path('', views.pagina_inicial, name='home'),
    path('contatos/', views.contato_lista, name='contato_lista'),
    path('contatos/novo', views.contato_criar, name='contato_criar'),
    path('contatos/<int:pk>/', views.contato_detalhe, name='contato_detalhe'),
    path('contatos/<int:pk>/editar', views.contato_editar, name='contato_editar'),
    path('contatos/<int:pk>/apagar', views.contato_apagar, name='contato_apagar'),
]