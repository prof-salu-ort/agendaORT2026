from django.db import models
from django.db.models import CharField


# Create your models here.
#ORM --> Object-Relational Mapper

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    #Criando o campo nome, com max de 255 caracteres, preenchimento obrigatorio
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    categoria = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag, blank=True)

    foto = models.ImageField(upload_to='fotos_contatos/', blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.nome} [{self.email}]'