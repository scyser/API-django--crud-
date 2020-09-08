from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer


@api_view(['POST', 'DELETE'])
def user_all(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data["id"])
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        users = User.objects.all()
        for user in users:
            user.is_deleted = True
            user.save()
        return Response('{}')


@api_view(['GET', 'PUT', 'DELETE'])
def user_id(request, pk):
    try:
        user = User.objects.get(pk=pk)
        if user.is_deleted:
            raise User.DoesNotExist
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('{}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.is_deleted = True
        user.save()
        return Response('{}')


@api_view(['GET', 'POST', 'DELETE'])
def task_all(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks = tasks.filter(is_deleted=False)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data["id"])
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tasks = Task.objects.all()
        for task in tasks:
            task.is_deleted = True
            task.save()
        return Response('{}')


@api_view(['GET', 'PUT', 'DELETE'])
def task_id(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        if task.is_deleted:
            raise Task.DoesNotExist
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('{}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.is_deleted = True
        task.save()
        return Response('{}')



