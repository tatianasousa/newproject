from django.forms import ModelForm
from newapp.models import *
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class EscolaForm(ModelForm):
    class Meta:
        model = Escola
        fields = ['nome']

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"
        widgets = {
            'dt_nascimento' : forms.DateInput(attrs={'type':'date'})
        }

class AtorForm(ModelForm):
    class Meta:
        model = Ator
        fields = ['nome']
    
class FilmeForm(ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'