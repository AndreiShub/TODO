from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    return HttpResponse("<h1>Hello World!</h1>")

def about_page(request):
    return HttpResponse("<h1>About</h1>")