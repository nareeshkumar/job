from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    return render(request,'App1/index.html')

def PuneJobPortal(request):
    list=models.PuneJobPortal.objects.all()
    dict={'list':list}
    return render(request,'App1/PuneJobPortal.html',context=dict)
def BangaloreJobPortal(request):
    list=models.BangaloreJobPortal.objects.all()
    dict={'list':list}
    return render(request,'App1/BangaloreJobPortal.html',context=dict)
def ChennaiJobPortal(request):
    list=models.ChennaiJobPortal.objects.all()
    dict={'list':list}
    return render(request,'App1/ChennaiJobPortal.html',context=dict)
def HydJobPortal(request):
    list=models.HydJobPortal.objects.all()
    dict={'list':list}
    return render(request,'App1/HydJobPortal.html',context=dict)