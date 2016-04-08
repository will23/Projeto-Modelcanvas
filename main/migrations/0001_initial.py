# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Negocio'
        db.create_table(u'main_negocio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('criado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('atualizado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('proposta_valor', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('parceiros_chave', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('atividades_chave', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('recursos_chave', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('relacionamento_clientes', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('segmentos_clientes', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('canais', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('estrutura_custos', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('fontes_receita', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Negocio'])


    def backwards(self, orm):
        # Deleting model 'Negocio'
        db.delete_table(u'main_negocio')


    models = {
        u'main.negocio': {
            'Meta': {'object_name': 'Negocio'},
            'atividades_chave': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'atualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'canais': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'criado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'estrutura_custos': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'fontes_receita': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'parceiros_chave': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'proposta_valor': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'recursos_chave': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'relacionamento_clientes': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'segmentos_clientes': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']