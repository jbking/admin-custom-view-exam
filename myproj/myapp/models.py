from django.db import models


class Token(models.Model):
    data = models.CharField(max_length=1024)
    enable = models.BooleanField()
