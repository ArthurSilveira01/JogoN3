from django.db import models

# Create your models here.

class Jogo(models.Model):
    titulo = models.CharField(max_length=255)
    desenvolvedora = models.CharField(max_length=20, blank=True, null=True)
    ano_publicacao = models.IntegerField(max_length=255, blank=True, null=True)
    plataforma = models.CharField(blank=True, null=True)

    def __str__(self):
        return f'{self.nome}[{self.email}]'

