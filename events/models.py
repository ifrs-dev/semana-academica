from django.db import models
from django.contrib.auth.models import User

CHOICES_STATUS_REGISTRATION = (
    (1, "Inscrito"),
    (2, "Presente"),
    (3, "Ausente")
)


class Registration(models.Model):

    class Meta:

        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='registrations')
    status = models.IntegerField(choices=CHOICES_STATUS_REGISTRATION, default=1)
    paid = models.BooleanField(default=False)
