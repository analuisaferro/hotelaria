from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Regiao(models.Model):
    nome=models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')

    def __str__(self):
        return '%s' % (self.nome)

    class Meta:
        ordering = ['nome']

class Hospedagem(models.Model):
    regiao=models.ForeignKey(Regiao, on_delete=models.CASCADE, verbose_name='Região')
    nome=models.CharField(max_length=150)
    n_cadastur=models.IntegerField('Nº do Cadastur')
    telefone=models.CharField(max_length=11)
    n_total_uh=models.IntegerField('Nº total de UH')
    n_total_leitos=models.IntegerField('Nº total de Leitos')    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')

    def __str__(self):
        return '%s' % (self.nome)

    class Meta:
        ordering = ['regiao', 'nome']

class Ocupacao(models.Model):
    hospedagem=models.ForeignKey(Hospedagem, on_delete=models.CASCADE)
    n_uh_ocupados=models.IntegerField('Nº UH ocupados')    
    n_leitos_ocupados=models.IntegerField('Nº Leitos ocupados')    
    obs=models.CharField(max_length=150, verbose_name='Observação')
    dt_1 = models.DateField('Data inicial')
    dt_2 = models.DateField('Data final')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')
    
    def __str__(self):
        return '%s - %s' % (self.hospedagem, self.n_uh_ocupados)

    class Meta:
        ordering = ['hospedagem']

