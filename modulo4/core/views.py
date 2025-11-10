from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa, Execucao
# Create your views here.
def home(request):
    todas_as_tarefas = Tarefa.objects.all()
    todas_as_execucoes = Execucao.objects.all()
    context={
        'nome_usuario':'Lorrane',
        'tecnologias':['python', 'Django','HTML','CSS'],
        'tarefas':todas_as_tarefas,
        'execucao':todas_as_execucoes
    }
    return render(request, 'home.html',context)
  
def site(request):
    return HttpResponse("<h1>Nova pasta</h1>")