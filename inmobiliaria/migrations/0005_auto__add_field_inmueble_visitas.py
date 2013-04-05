# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Inmueble.visitas'
        db.add_column(u'inmobiliaria_inmueble', 'visitas',
                      self.gf('django.db.models.fields.IntegerField')(default=34),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Inmueble.visitas'
        db.delete_column(u'inmobiliaria_inmueble', 'visitas')


    models = {
        u'inmobiliaria.imagen': {
            'Meta': {'object_name': 'Imagen'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inmueble': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmobiliaria.Inmueble']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ruta': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'inmobiliaria.inmueble': {
            'Meta': {'object_name': 'Inmueble'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'banos': ('django.db.models.fields.IntegerField', [], {}),
            'contenido': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fecha_insert': ('django.db.models.fields.DateField', [], {}),
            'habitaciones': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'metros_casa': ('django.db.models.fields.IntegerField', [], {}),
            'metros_jardin': ('django.db.models.fields.IntegerField', [], {}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'visitas': ('django.db.models.fields.IntegerField', [], {}),
            'zona': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['inmobiliaria']