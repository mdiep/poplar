# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Group'
        db.create_table('poplar_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=30, unique=True)),
        ))
        db.send_create_signal('poplar', ['Group'])

        # Adding M2M table for field people on 'Group'
        db.create_table('poplar_group_people', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['poplar.group'], null=False)),
            ('person', models.ForeignKey(orm['poplar.person'], null=False))
        ))
        db.create_unique('poplar_group_people', ['group_id', 'person_id'])


    def backwards(self, orm):
        
        # Deleting model 'Group'
        db.delete_table('poplar_group')

        # Removing M2M table for field people on 'Group'
        db.delete_table('poplar_group_people')


    models = {
        'poplar.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'unique': 'True'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'groups'", 'symmetrical': 'False', 'to': "orm['poplar.Person']"})
        },
        'poplar.person': {
            'Meta': {'object_name': 'Person'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['poplar']
