from django.db import models
from django.conf import settings

class Schedule(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='schedules')
    psycologist = models.ForeignKey('Psycologist', on_delete=models.CASCADE, related_name='schedules')
    date = models.DateTimeField()

    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"

    def __str__(self):
        return f'{self.patient.name} - {self.psycologist}'
