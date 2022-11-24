from django.db import models
from django.conf import settings

class Patients(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=200)
    description = models.TextField("Descrição")

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return self.name
