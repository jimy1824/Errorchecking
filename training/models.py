from django.db import models

from django.db import models


# Create your models here.

class ERRORTYPE(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    error_title = models.CharField(max_length=500)
    max_value = models.FloatField()
    avg_value = models.FloatField()

    def __str__(self):
        return str(self.error_title)