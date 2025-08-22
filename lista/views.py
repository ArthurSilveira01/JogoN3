from django.shortcuts import render

# Create your views here.

def lista_jogos(request):
    jogo = Contato.objects.all().order_by('nome')
    return render(request,
              'agenda/lista_jogos.html',
              {'jogo' : jogo})

def lista_jogos_http(request):
    return HttpResponse(
        ''' 
            <h1>Lista de jogos</h1>
        ''')



def create(request):
    if request.method == 'POST':
        form = JogoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista:lista_jogos')
    else:
        form = JogoForm()
        return render(request,
                      'lista/create_jogo.html',
                      {'form' : form,
                      'titulo_pagina': 'Adicionar Jogos'})

def jogo_detalhe(request, pk):
    jogo = get_object_or_404(Jogo, pk)

    return render(request, 'lista/jogo_detalhe.html', {'jogo' : jogo})

def jogo_editar(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        form = JogoForm(request.POST, instance=jogo)

        if form.is_valid():
            form.save()
            return redirect('lista:jogo_detalhe', pk=jogo.pk)
    else:
        form = JogoForm(instace=jogo)

    return render(request,
                  'lista/create_jogo.hmtl',
                  {'form' : form, 'jogo' : jogo, 'titulo_pagina' : 'Editar'})

def jogo_excluir(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)

    if request.method == 'POST':
        jogo.delete()
        return redirect('lista:lista_jogos')
    return render(request,
                  'lista/jogo_confirma_exclusao.html',
                  {'jogo' : jogo})
