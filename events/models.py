from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CHOICES_STATUS_REGISTRATION = (
    (1, "Inscrito"),
    (2, "Pago"),
    (3, "Presente"),
    (0, "Ausente")
)





class Registration(models.Model):

    class Meta:

        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    user = models.ForeignKey(User, unique=True, on_delete=models.PROTECT, related_name='registrations')
    status = models.IntegerField(choices=CHOICES_STATUS_REGISTRATION, default=1)