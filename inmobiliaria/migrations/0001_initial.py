# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Imagen'
        db.create_table(u'inmobiliaria_imagen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ruta', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'inmobiliaria', ['Imagen'])

        # Adding model 'Inmueble'
        db.create_table(u'inmobiliaria_inmueble', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_insert', self.gf('django.db.models.fields.DateField')()),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('localidad', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('zona', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('banos', self.gf('django.db.models.fields.IntegerField')()),
            ('habitaciones', self.gf('django.db.models.fields.IntegerField')()),
            ('metros_casa', self.gf('django.db.models.fields.IntegerField')()),
            ('metros_jardin', self.gf('django.db.models.fields.IntegerField')()),
            ('contenido', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Imagenes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inmobiliaria.Imagen'])),
        ))
        db.send_create_signal(u'inmobiliaria', ['Inmueble'])


    def backwards(self, orm):
        # Deleting model 'Imagen'
        db.delete_table(u'inmobiliaria_imagen')

        # Deleting model 'Inmueble'
        db.delete_table(u'inmobiliaria_inmueble')


    models = {
        u'inmobiliaria.imagen': {
            'Meta': {'object_name': 'Imagen'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ruta': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'inmobiliaria.inmueble': {
            'Imagenes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmobiliaria.Imagen']"}),
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
            'zona': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['inmobiliaria']