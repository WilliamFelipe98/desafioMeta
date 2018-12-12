from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=500)
    canal = models.CharField(max_length=20)
    valor = models.CharField(max_length=20)
    obs = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) 
     
def __str__(self):
    return "Nome: "+self.nome+", Canal: "+ self.canal+", Valor: "+ self.valor+", Observação: "+ self.obs
