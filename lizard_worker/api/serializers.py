from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from lizard_worker.models import WorkflowTask


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'users': reverse('user-list', request=request),
        'groups': reverse('group-list', request=request),
    })


class WorkflowTaskSerializer(serializers.ModelSerializer):
    code = serializers.Field(source='code.name')
    scenario = serializers.Field(source='workflow.scenario')
    #execute_url = serializers.Field(source='get_absolute_url_start_task')
    class Meta:
        model = WorkflowTask
        exclude = ('parent_code', 'template')
