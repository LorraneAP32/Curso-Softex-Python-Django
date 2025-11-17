from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.home,
        name='home',),
    # <int:pk> captura um inteiro da URL e o passa para a view como um argumento chamado 'pk'
    path('tarefa/<int:pk>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    # Ex: /tarefa/5/deletar/
    path('tarefa/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),

    path(
        'site/',
        views.site,
        name='site',),
]