from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):

    class Meta:
        verbose_name = 'Minicurso'
        verbose_name_plural = 'Minicursos'

    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Resumo (Breve descrição)', help_text='Paragráfo único com no máximo 100 palavras.')
    goal = models.TextField(verbose_name='Objetivo')
    public = models.CharField(max_length=200, verbose_name='Público Alvo')
    vacancies = models.PositiveIntegerField(verbose_name='Número Máximo de Participantes')
    requirements = models.TextField(verbose_name='Pré-requisitos', blank=True, null=True)
    materials = models.TextField(verbose_name='Recursos necessários', blank=True, null=True)
    workload = models.PositiveIntegerField(verbose_name='Carga Horária')
    status = models.IntegerField(default=1, verbose_name='Status')
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.PROTECT, related_name='author_events')
    co_authors = models.ManyToManyField(User, verbose_name='Co-autores', related_name='co_authors_events', blank=True)
    supervisor = models.ForeignKey(User, verbose_name='Orientador', on_delete=models.PROTECT, related_name='supervised_events', blank=True, null=True)
