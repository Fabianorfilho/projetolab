from django.db import models
from django.contrib.auth.models import User


class TiposExames(models.Model):
    
    tipo_choice = (
        ('I', 'Exame de imagem'),
        ('S', 'Exame de sangue')
    )
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, choices=tipo_choice)
    preco = models.FloatField()
    disponivel = models.BooleanField(default=True)
    horario_inicial = models.IntegerField()
    horario_final = models.IntegerField()
    
    def __str__(self):
        return self.nome
        

    
class SolicitacaoExame(models.Model):
    choice_status = (
        ('E', 'Em análise'),
        ('F', 'Finalizado')
    )
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    exame = models.ForeignKey(TiposExames, on_delete=models.DO_NOTHING)
    status  = models.CharField(max_length=2, choices=choice_status)
    resultado = models.FileField(upload_to="resultados", null=True, blank=True)
    requer_senha = models.BooleanField(default=False)
    senha = models.CharField(max_length=6, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    avaliacao = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.usuario } | {self.exame.nome}'
    
class PedidoExame(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    exames = models.ManyToManyField(SolicitacaoExame)
    agendado = models.BooleanField(default=True)
    data = models.DateField()
    
    def __str__(self):
        return f'{self.usuario} | {self.data}'
    

