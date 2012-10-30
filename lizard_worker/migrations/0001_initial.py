# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'WorkflowTemplate'
        db.create_table('lizard_worker_workflowtemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.IntegerField')(max_length=30)),
        ))
        db.send_create_signal('lizard_worker', ['WorkflowTemplate'])

        # Adding model 'Workflow'
        db.create_table('lizard_worker_workflow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_worker.WorkflowTemplate'], null=True, blank=True)),
            ('scenario', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tcreated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('tstart', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('tfinished', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('logging_level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('lizard_worker', ['Workflow'])

        # Adding model 'TaskType'
        db.create_table('lizard_worker_tasktype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('lizard_worker', ['TaskType'])

        # Adding model 'WorkflowTemplateTask'
        db.create_table('lizard_worker_workflowtemplatetask', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_worker.TaskType'])),
            ('parent_code', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parent_task_code', null=True, to=orm['lizard_worker.TaskType'])),
            ('max_failures', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('max_duration_minutes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('workflow_template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_worker.WorkflowTemplate'])),
        ))
        db.send_create_signal('lizard_worker', ['WorkflowTemplateTask'])

        # Adding model 'WorkflowTask'
        db.create_table('lizard_worker_workflowtask', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workflow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_worker.Workflow'])),
            ('code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_worker.TaskType'])),
            ('parent_code', self.gf('django.db.models.fields.related.ForeignKey')(related_name='workflowtask_parent_task_code', null=True, to=orm['lizard_worker.TaskType'])),
            ('max_failures', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('max_duration_minutes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tcreated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('tqueued', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('tstart', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('tfinished', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('successful', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
        ))
        db.send_create_signal('lizard_worker', ['WorkflowTask'])

        # Adding model 'Worker'
        db.create_table('lizard_worker_worker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('worker_nr', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('node', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('queue_code', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
        ))
        db.send_create_signal('lizard_worker', ['Worker'])

        # Adding model 'Logging'
        db.create_table('lizard_worker_logging', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workflow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_worker.Workflow'], null=True, blank=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_worker.WorkflowTask'], null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('worker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_worker.Worker'], null=True, blank=True)),
            ('is_heartbeat', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('lizard_worker', ['Logging'])


    def backwards(self, orm):
        
        # Deleting model 'WorkflowTemplate'
        db.delete_table('lizard_worker_workflowtemplate')

        # Deleting model 'Workflow'
        db.delete_table('lizard_worker_workflow')

        # Deleting model 'TaskType'
        db.delete_table('lizard_worker_tasktype')

        # Deleting model 'WorkflowTemplateTask'
        db.delete_table('lizard_worker_workflowtemplatetask')

        # Deleting model 'WorkflowTask'
        db.delete_table('lizard_worker_workflowtask')

        # Deleting model 'Worker'
        db.delete_table('lizard_worker_worker')

        # Deleting model 'Logging'
        db.delete_table('lizard_worker_logging')


    models = {
        'lizard_worker.logging': {
            'Meta': {'object_name': 'Logging'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_heartbeat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_worker.WorkflowTask']", 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_worker.Worker']", 'null': 'True', 'blank': 'True'}),
            'workflow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_worker.Workflow']", 'null': 'True', 'blank': 'True'})
        },
        'lizard_worker.tasktype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'TaskType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'lizard_worker.worker': {
            'Meta': {'object_name': 'Worker'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'queue_code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'worker_nr': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'lizard_worker.workflow': {
            'Meta': {'object_name': 'Workflow'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logging_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scenario': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tcreated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_worker.WorkflowTemplate']", 'null': 'True', 'blank': 'True'}),
            'tfinished': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tstart': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'lizard_worker.workflowtask': {
            'Meta': {'object_name': 'WorkflowTask'},
            'code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_worker.TaskType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_duration_minutes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'max_failures': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent_code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'workflowtask_parent_task_code'", 'null': 'True', 'to': "orm['lizard_worker.TaskType']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'successful': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'tcreated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tfinished': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tqueued': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tstart': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'workflow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_worker.Workflow']"})
        },
        'lizard_worker.workflowtemplate': {
            'Meta': {'object_name': 'WorkflowTemplate'},
            'code': ('django.db.models.fields.IntegerField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lizard_worker.workflowtemplatetask': {
            'Meta': {'object_name': 'WorkflowTemplateTask'},
            'code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_worker.TaskType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_duration_minutes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'max_failures': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent_code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parent_task_code'", 'null': 'True', 'to': "orm['lizard_worker.TaskType']"}),
            'workflow_template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_worker.WorkflowTemplate']"})
        }
    }

    complete_apps = ['lizard_worker']
