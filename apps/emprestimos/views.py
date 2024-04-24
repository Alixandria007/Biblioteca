from django.shortcuts import render, redirect
import datetime
from apps.leitores.models import Leitor
from apps.livros.models import Genero,Autor,Livros
from django.core.paginator import Paginator
from django.contrib import messages
from . import models
# Create your views here.

def criar_emprestimo(request):

    if not request.session['leitor']:

        messages.error(
            request,
            'Não há leitor definido para poder criar o emprestimo.'
        )

        return redirect('livros:realizar_emprestimo')
    
    if not request.session.get('previa_emprestimo'):
        messages.error(
            request,
            'Não há livros em sua previa.'
        )

        return redirect('livros:index')
    

    leitor = Leitor.objects.filter(leitor__username = request.session['leitor']).first()
    previa = request.session['previa_emprestimo']

    genero_ids = {}
    for k in previa.keys():
        genero_ids[k] = ({k: [genero_id['id'] for genero_id in previa[k]['genero']]})
    
    print(genero_ids.values())
        
    data_final = request.GET.get('data-final')

    emprestimo = models.Emprestimo(
        leitor = leitor,
        data_inicial = datetime.date.today().isoformat(),
        data_final = data_final,
        quant_livros = len(previa),
        status = 'C'
    )

    emprestimo.save()


    models.LivroEmprestimo.objects.bulk_create(
        models.LivroEmprestimo(
            emprestimo = emprestimo,
            nome = l['nome'],
            livro_id = l['id'],
            slug = l['slug'],
            sinopse = l['sinopse_curta'],
            quantidade = 1,
            paginas = l['paginas'],
            autor = Autor.objects.filter(nome = l['autor']).first(),
            imagem = l['imagem']
        ) for l in previa.values()
    )

    messages.success(
        request,
        f'Emprestimo do leitor {leitor.leitor.first_name} Criado.'
    )

    del request.session['previa_emprestimo']
    
    return redirect('livros:index')


def consultar_emprestimos(request):
    emprestimos = models.Emprestimo.objects.all()

    paginator = Paginator(emprestimos, 10)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    context = {
        'emprestimos' : page_obj,
        'search_emprestimo' : True,
    }
    

    return render(request, 'consultar_emprestimo.html', context)

def emprestimo(request, id):
    emprestimo_ = models.Emprestimo.objects.filter(id = id).first()

    livro_emprestimo = models.LivroEmprestimo.objects.filter(emprestimo__id = id).all()

    context = {
        'emprestimo': emprestimo_,
        'livros': livro_emprestimo,
        'search_leitor' : True,
    }

    return render(request, 'emprestimo.html', context)