from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    water_intake = models.IntegerField(help_text="Water intake in millilitres")
    step_count = models.IntegerField(help_text="Number of steps")

    def __str__(self):
        return f"{self.user.username} - {self.date}"
