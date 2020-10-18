"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from newapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_post/', views.add_post, name='add_post'),
    path('', views.list_posts, name='list_posts'),
    path('add_escola/', views.add_escola, name='add_escola'),
    path('list_escolas/', views.list_escolas, name='list_escolas'),
    path('add_aluno/', views.add_aluno, name='add_aluno'),
    path('list_alunos/', views.list_alunos, name='list_alunos'),
    path('add_ator/', views.add_ator, name='add_ator'),
    path('list_atores/', views.list_atores, name='list_atores'),
    path('add_filme/', views.add_filme, name='add_filme'),
    path('list_filmes/', views.list_filmes, name='list_filmes'),
]
