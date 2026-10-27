from django.shortcuts import render, redirect
from .models import Tasks
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from  .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
@login_required
def home(request):
    if request.method == "POST":
        title = request.POST["task_name"]
        Tasks.objects.create(name=title, owner=request.user)
        return redirect("/")
    tasks = Tasks.objects.filter(owner=request.user)

    return render(request , "tasks/home.html", {"tasks": tasks})

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def api_tasks(request):
    tasks = Tasks.objects.filter(owner=request.user)
    serializer = TaskSerializer(tasks, many=True)
    if request.method == "POST":
        client_data = TaskSerializer(data=request.data)
        if client_data.is_valid():
            client_data.save(owner=request.user)
            return Response(client_data.data, status=status.HTTP_201_CREATED)     
        else:
            return Response(client_data.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data)
@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def api_task_detail(request, pk):
    task = Tasks.objects.filter(owner=request.user, id=pk).first()
    if task is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    if request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == "PATCH":
        patch = TaskSerializer(task, data=request.data, partial=True)
        if patch.is_valid():
            patch.save()
            return Response(patch.data)
        else:
            return Response(patch.errors, status=status.HTTP_400_BAD_REQUEST)











