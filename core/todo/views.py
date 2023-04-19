from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

tasks = {"1": "asfasdff", "2": "qqqqqqqqq"}


def main_page(request):
    todos = Todo.objects.all()
    print(todos)
    return render(request, "index.html", {"todos": todos})

