# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Inmueble.fecha_insert'
        db.alter_column(u'inmobiliaria_inmueble', 'fecha_insert', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # Changing field 'Inmueble.fecha_insert'
        db.alter_column(u'inmobiliaria_inmueble', 'fecha_insert', self.gf('django.db.models.fields.DateField')(default=''))

    models = {
        u'inmobiliaria.imagen': {
            'Meta': {'object_name': 'Imagen'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inmueble': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmobiliaria.Inmueble']", 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ruta': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'inmobiliaria.inmueble': {
            'Meta': {'object_name': 'Inmueble'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'banos': ('django.db.models.fields.IntegerField', [], {}),
            'contenido': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fecha_insert': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'habitaciones': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'metros_casa': ('django.db.models.fields.IntegerField', [], {}),
            'precio': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'provincia': ('django.db.models.fields.CharField', [], {'default': "'Madrid'", 'max_length': '30'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'Alquiler'", 'max_length': '2'}),
            'visitas': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'zona': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['inmobiliaria']