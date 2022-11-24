from django.db import models
from django.conf import settings

class Psychologist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    number = models.CharField('Numero', max_length=50)
    name = models.CharField('Nome', max_length=200)
    description = models.TextField("Descrição")

    class Meta:
        verbose_name = "Psychologist"
        verbose_name_plural = "Psychologists"

    def __str__(self):
        return self.name
