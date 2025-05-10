from django.db import models
from datetime import datetime

class Fotografia(models.Model):
    
    opcoes_categoria = [
        ('Nebulosa', 'nebulosa'),
        ('Estrela', 'estrela'),
        ('Galáxia', 'galaxia'),
        ('Planeta', 'planeta'),
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.CharField(choices=opcoes_categoria, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    publicada = models.BooleanField(default=False)
    data_publicacao = models.DateField(default=datetime.now, blank=False)
    
    def __str__(self):
        return self.nome
