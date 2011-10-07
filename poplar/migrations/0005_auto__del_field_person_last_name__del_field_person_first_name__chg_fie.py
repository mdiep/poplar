# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Person.last_name'
        db.delete_column('poplar_person', 'last_name')

        # Deleting field 'Person.first_name'
        db.delete_column('poplar_person', 'first_name')

        # Changing field 'Person.name'
        db.alter_column('poplar_person', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))


    def backwards(self, orm):
        
        # We cannot add back in field 'Person.last_name'
        raise RuntimeError(
            "Cannot reverse this migration. 'Person.last_name' and its values cannot be restored.")

        # We cannot add back in field 'Person.first_name'
        raise RuntimeError(
            "Cannot reverse this migration. 'Person.first_name' and its values cannot be restored.")

        # Changing field 'Person.name'
        db.alter_column('poplar_person', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))


    models = {
        'poplar.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'groups'", 'blank': 'True', 'to': "orm['poplar.Person']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'})
        },
        'poplar.person': {
            'Meta': {'object_name': 'Person'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['poplar']
