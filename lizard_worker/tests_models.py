"""Test for lizard_worker/models.py."""

from __future__ import unicode_literals

import factory

from lizard_worker import models

class WorkflowTemplateF(factory.Factory):
    FACTORY_FOR = models.WorkflowTemplate

    code = models.WorkflowTemplate.DEFAULT_TEMPLATE_CODE


class WorkflowF(factory.Factory):
    FACTORY_FOR = models.Workflow

    template = factory.SubFactory(WorkflowTemplateF)
    code = "Test code"
    scenario = 1


class TaskTypeF(factory.Factory):
    FACTORY_FOR = models.TaskType
    name = "120"


class WorkflowTemplateTaskF(factory.Factory):
    FACTORY_FOR = models.WorkflowTemplateTask
    
    workflow_template = factory.SubFactory(WorkflowTemplateF)
    code = factory.SubFactory(TaskTypeF)
    parent_code = factory.SubFactory(TaskTypeF)


class WorkflowTaskF(factory.Factory):
    FACTORY_FOR = models.WorkflowTask

    workflow = factory.SubFactory(WorkflowF)
    code = factory.SubFactory(TaskTypeF)
    parent_code = factory.SubFactory(TaskTypeF)


class WorkerF(factory.Factory):
    FACTORY_FOR = models.Worker

    worker_nr = 1


class LoggingF(factory.Factory):
    FACTORY_FOR = models.Logging

    workflow = factory.SubFactory(WorkflowF)
    task = factory.SubFactory(WorkflowTaskF)
    worker = factory.SubFactory(WorkerF)
