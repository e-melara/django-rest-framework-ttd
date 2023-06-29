from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Puppy


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_puppy(request, pk):
    try:
        puppy = Puppy.objects.get(pk=pk)
    except Puppy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({})
    elif request.method == 'DELETE':
        return Response({})
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_puppies(request):
    if request.method == 'GET':
        return Response({})
    elif request.method == 'POST':
        return Response({})
