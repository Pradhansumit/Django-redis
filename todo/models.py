from django.db import models

class TodoModel(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
