Changelog of lizard-worker
===================================================


0.12 (unreleased)
-----------------

- Nothing changed yet.


0.11 (2014-08-21)
-----------------

- Upgraded everything to Django 1.6.6.


0.10 (2012-12-06)
-----------------

- Nothing changed yet.


0.9 (2012-11-26)
----------------

- Remove amqp-logging-handler from action object after executing of workflow, task.

- Pinned to pika >= 0.9.8


0.8 (2012-11-15)
----------------

- Removed 'heartbeat' connection parameter due update in pika 0.9.6.

- Pinned to pika >= 0.9.7.

0.7 (2012-10-30)
----------------

- Created migration schemas (fake initial schema on update).


0.6 (2012-10-30)
----------------

- Added default value to scenario_type in body.

- Added scenario_type field to Workflow model.


0.5 (2012-10-23)
----------------

- Added tests.

- Fixed error in reque_failed_message function by empty MAX_FEAILURE_TMP dict in body.


0.4 (2012-10-22)
----------------

- Fixed boolean -> bool bug in action_task.

- Added scenario_type to start_workflow and ActionWorkflow.

- Default queue name for task code Action.retrieve_queue_options.

- Added get_absolute_url for workflow.


0.3 (2012-10-17)
----------------

Replaced the parameter 'scenario_id' with 'body' in callback function of
'action_task' module.


0.2 (2012-10-16)
----------------

- Use simplejson from django.utils.


0.1 (2012-10-16)
----------------

- Initial project structure created with nensskel 1.26.

- Transform flooding-worker to lizard-worker.

- Move tasks and perform_task.py to flooding-lib.

- Rename management commands, add help text.
