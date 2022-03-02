from sqlite3 import Timestamp
from django.db import models

# Create your models here.


class Form(models.Model):
    inp1 = models.TextField()
    inp2 = models.TextField()
    inp3 = models.TextField()
    inp4 = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True, blank=True)


   # def __str__(self):
   #     return 'Input At' + self.Timestamp