from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.http import HttpResponse

def home(request):
    html = """
    <h1 align="center">Hello my site</h1>
    """
    return HttpResponse(html)
