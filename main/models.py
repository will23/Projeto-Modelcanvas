# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_text

# Create your models here.
class Negocio (models.Model):
    nome = models.CharField(max_length=80)
    autor = models.CharField(max_length=80)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    proposta_valor = models.CharField(max_length=80, null=True, blank=True)
    parceiros_chave = models.CharField(max_length=80, null=True, blank=True)
    atividades_chave = models.CharField(max_length=80, null=True, blank=True)
    recursos_chave = models.CharField(max_length=80, null=True, blank=True)
    relacionamento_clientes = models.CharField(max_length=80, null=True, blank=True)
    segmentos_clientes = models.CharField(max_length=80, null=True, blank=True)
    canais = models.CharField(max_length=80, null=True, blank=True)
    estrutura_custos = models.CharField(max_length=80, null=True, blank=True)
    fontes_receita = models.CharField(max_length=80, null=True, blank=True)

    def __unidode__(self):
        return self.nome + ' - ' + self.autor

    class Meta:
        verbose_name = "Negócio"
        verbose_name_plural = "Negócios"
