from django.shortcuts import render, redirect
from newapp.forms import *
from newapp.models import *

def list_posts(request):
    posts = Post.objects.all()
    return render(request, "list_posts.html", {'posts':posts})

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_posts')
    else:
            form = PostForm()
            return render(request, "add.html", {'form':form})

def list_escolas(request):
    escolas = Escola.objects.all()
    return render(request, "list_escola.html", {'escolas':escolas})

def list_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, "list_alunos.html", {'alunos':alunos})

def add_escola(request):
    if request.method == "POST":
        form = EscolaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_escolas')
    else:
        form = EscolaForm()
        return render(request, "add.html", {'form':form})

def add_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_alunos')
    else:
        form = AlunoForm()
        return render(request, "add.html", {'form':form})

def list_atores(request):
    atores = Ator.objects.all()
    return render(request, "list_atores.html", {'atores':atores})

def list_filmes(request):
    filmes = Filme.objects.all()
    return render(request, "list_filmes.html", {'filmes':filmes})

def add_ator(request):
    if request.method == "POST":
        form = AtorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_atores')
    else:
        form = AtorForm()
        return render(request, "add.html", {'form':form})

def add_filme(request):
    if request.method == "POST":
        form = FilmeForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_filmes')
    else:
        form = FilmeForm()
        return render(request, "add.html", {'form':form})