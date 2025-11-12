from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarefa, Execucao
from .forms import TarefaForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = TarefaForm()
    todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em')
    context = {
        'nome_usuario': 'Lorrane',
        'tecnologias': ['Python', 'Django', 'Models', 'Forms'],
        'tarefas': todas_as_tarefas,
        'form': form,
    }
            
    return render(request, 'home.html', context)

            

        
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

