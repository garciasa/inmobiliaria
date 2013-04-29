# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Inmueble'
        db.create_table(u'inmobiliaria_inmueble', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_insert', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default='Alquiler', max_length=2)),
            ('provincia', self.gf('django.db.models.fields.CharField')(default='Madrid', max_length=30)),
            ('localidad', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('zona', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('banos', self.gf('django.db.models.fields.IntegerField')()),
            ('habitaciones', self.gf('django.db.models.fields.IntegerField')()),
            ('metros_casa', self.gf('django.db.models.fields.IntegerField')()),
            ('contenido', self.gf('django.db.models.fields.TextField')(max_length=250)),
            ('precio', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('visitas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'inmobiliaria', ['Inmueble'])

        # Adding model 'Imagen'
        db.create_table(u'inmobiliaria_imagen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ruta', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('inmueble', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inmobiliaria.Inmueble'], blank=True)),
        ))
        db.send_create_signal(u'inmobiliaria', ['Imagen'])


    def backwards(self, orm):
        # Deleting model 'Inmueble'
        db.delete_table(u'inmobiliaria_inmueble')

        # Deleting model 'Imagen'
        db.delete_table(u'inmobiliaria_imagen')


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
            'contenido': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
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
            'visitas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zona': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['inmobiliaria']