from django.db import models


class Frame(models.Model):
    text = models.CharField(max_length=1000)
