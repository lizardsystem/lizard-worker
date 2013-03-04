from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from lizard_worker.api.views import WorkflowTaskList


admin.autodiscover()
urlpatterns = patterns('',)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
# Default login/logout views
urlpatterns += patterns('lizard_worker.api.views',

    url(r'^tasks/$', WorkflowTaskList.as_view(),
        name='worker_workflow_task'),
    url(r'^tasks/execute\?task_id=(?P<task_id>\d+)$',
        WorkflowTaskList.as_view(),
        name='worker_start_task'),
)
