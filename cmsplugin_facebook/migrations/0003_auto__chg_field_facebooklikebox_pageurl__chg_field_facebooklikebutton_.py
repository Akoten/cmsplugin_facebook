# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FacebookLikeBox.pageurl'
        db.alter_column('cmsplugin_facebooklikebox', 'pageurl', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'FacebookLikeButton.pageurl'
        db.alter_column('cmsplugin_facebooklikebutton', 'pageurl', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'FacebookLikeBox.pageurl'
        raise RuntimeError("Cannot reverse this migration. 'FacebookLikeBox.pageurl' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'FacebookLikeButton.pageurl'
        raise RuntimeError("Cannot reverse this migration. 'FacebookLikeButton.pageurl' and its values cannot be restored.")

    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_facebook.facebooklikebox': {
            'Meta': {'object_name': 'FacebookLikeBox', 'db_table': "'cmsplugin_facebooklikebox'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'connections': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'header': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '587'}),
            'pageurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stream': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'transparent': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'cmsplugin_facebook.facebooklikebutton': {
            'Meta': {'object_name': 'FacebookLikeButton', 'db_table': "'cmsplugin_facebooklikebutton'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color_scheme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '50'}),
            'font': ('django.db.models.fields.CharField', [], {'default': "'verdana'", 'max_length': '50'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '80'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'standard'", 'max_length': '50'}),
            'pageurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'verb': ('django.db.models.fields.CharField', [], {'default': "'like'", 'max_length': '50'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'cmsplugin_facebook.facebooksharebutton': {
            'Meta': {'object_name': 'FacebookShareButton', 'db_table': "'cmsplugin_facebooksharebutton'", '_ormbases': ['cms.CMSPlugin']},
            'button_text': ('django.db.models.fields.CharField', [], {'default': "u'Share'", 'max_length': '255'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'share_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        }
    }

    complete_apps = ['cmsplugin_facebook']