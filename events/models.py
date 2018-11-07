from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CHOICES_STATUS_REGISTRATION = (
    (1, "Inscrito"),
    (2, "Presente"),
    (3, "Ausente"),
)


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
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.PROTECT, related_name='author_events')


class Registration(models.Model):

    class Meta:
        unique_together = (('event', 'user'),)
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='registrations')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='registrations')
    status = models.IntegerField(choices=CHOICES_STATUS_REGISTRATION, default=1)