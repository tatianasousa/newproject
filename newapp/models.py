from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Escola(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=200)
    sexo = models.CharField(max_length=10)
    dt_nascimento = models.DateTimeField()
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Ator(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.CharField(max_length=4)
    atores = models.ManyToManyField(Ator)

    def __str__(self):
        return self.titulo