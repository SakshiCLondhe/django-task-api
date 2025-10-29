from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
import requests

# ------------------- CRUD API (REST Framework) -------------------
class TaskListCreateView(generics.ListCreateAPIView):
    """
    List all tasks or create a new task.
    """
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# ------------------- 3rd Party API (Random User) -------------------
@api_view(['GET'])
def get_random_user(request):
    """
    Fetches a random user from the RandomUser API.
    """
    try:
        res = requests.get("https://randomuser.me/api/", timeout=5)
        res.raise_for_status()
        data = res.json()['results'][0]
        return Response({
            "name": f"{data['name']['first']} {data['name']['last']}",
            "email": data['email'],
            "country": data['location']['country']
        })
    except Exception as e:
        return Response({"error": str(e)}, status=400)


# ------------------- Chart View -------------------
@api_view(['GET'])
def show_task_chart(request):
    """
    Displays a simple chart of completed vs pending tasks.
    """
    tasks = Task.objects.all()
    completed = tasks.filter(completed=True).count()
    pending = tasks.filter(completed=False).count()

    return render(request, 'chart.html', {
        'completed': completed,
        'pending': pending
    })


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')