from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contato
from .forms import ContatoForm

# Create your views here.
def ola_mundo(request):
    return HttpResponse('<p>Olá! Está é minha primeira view com DJANGO!</p>')

def pagina_inicial(request):
    return render(request, 'agenda/index.html')

#Retorna todos os contatos da agenda
def contato_lista(request):
    #ORM (Object-Relational Mapping)
    contatos = Contato.objects.all()
    #Renderiza o html passando a lista de contatos
    return render(request, 'agenda/contatos_lista.html', {'contatos' : contatos})

def contato_criar(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:contato_lista')
    else:
        form = ContatoForm()

    return render(request, 'agenda/contato_form.html', {'form' : form})

def contato_detalhe(request, pk):
    #tenta pegar o contato pela pk caso contrario retorna o erro 404
    contato = get_object_or_404(Contato, pk=pk)
    #Envia o contato encontrado para o HTML
    return render(request, 'agenda/contato_detalhe.html', {'contato' : contato})

def contato_editar(request, pk):
    #Busca o contato no banco de dados
    contato = get_object_or_404(Contato, pk=pk)

    if request.method == 'POST':
        #Passa os dados novos e avisa qual contato atualizar
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('agenda:contato_detalhe', pk=contato.pk)
    else:
        #cria o form preenchido com os dados do contato
        form = ContatoForm(instance=contato)
    return render(request, 'agenda/contato_form.html', {'form' : form})


def contato_apagar(request, pk):
    contato = get_object_or_404(Contato, pk=pk)

    if request.method == 'POST':
        contato.delete()
        return redirect('agenda:contato_lista')

    return render(request, 'agenda/contato_confirmar_exclusao.html', {'contato' : contato})