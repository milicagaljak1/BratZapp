from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

# Create your views here.


# def index(request):
#     return HttpResponse("Hello world!")

def index(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

# def index(request):
#   mymembers = Members.objects.all().values()
#   output = ""
#   for x in mymembers:
#     output += x["firstname"]
#     output += '\n'
#   return HttpResponse(output)