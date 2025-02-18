from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_overview(request):
    api_urls={
    'GET TASKS': 'get/tasks/',
    'ADD TASKS': 'post/tasks/',
    'UPDATE TASKS': 'put/tasks/<int:id>/',
    'DELETE TASKS': 'delete/tasks/<int:id>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def get_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many= True)
        return Response(serializer.data)
    
  

@api_view(['POST'])
def add_task(request):
    serializer = TaskSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['GET','PUT'])
def update_tasks(request, id):
    task = Task.objects.get(id = id)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = TaskSerializer(task, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
@api_view(['DELETE','GET'])
def delete_tasks(request, id):    
    task = Task.objects.get(id = id)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    task.delete()
    return Response("DELETED SUCCESFULLY")
    
    
        
    
    
