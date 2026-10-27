from django.db import models
from django.contrib.auth.models import User
class Tasks(models.Model):
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

