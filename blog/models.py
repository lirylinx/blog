from django.db import models
from django.utils import timezone


class Post(models.Model):
  autor = models.ForeignKey('auth.User')
  titulo = models.CharField(max_length=200)
  texto = models.TextField()
  data_criado = models.DateTimeField(default=timezone.now)
  data_publicado = models.DateTimeField(blank=True, null=True)


def pZZublicado(self):
  self.data_publicado = timezone.now()
  self.save()

def __str__(self):
  return self.title


