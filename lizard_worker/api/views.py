from django.http import HttpResponse

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.renderers import JSONRenderer

from lizard_worker.api.serializers import WorkflowTaskSerializer
from lizard_worker.models import WorkflowTask
from lizard_worker.models import Workflow

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class WorkflowTaskList(generics.ListCreateAPIView):

    def get(self, request, format=None):
        scenario_id = request.GET.get('scenario_id', -999)
        workflows = Workflow.objects.filter(scenario=scenario_id)
        tasks = WorkflowTask.objects.filter(workflow__in=workflows)
        serializer =  WorkflowTaskSerializer(tasks)
        return JSONResponse(serializer.data)
    

# class WorkflowTaskList(APIView):

#     def get(self, request, format=None):
#         """
#         Return a list of tasks.
#         """
#         tasks = WorkflowTasks.

