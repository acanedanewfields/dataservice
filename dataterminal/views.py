from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
     return render(request,'dataterminal/dashboard_sufee.html')

def fieldmap(request):
    return render(request,'dataterminal/fieldmap.html')    

def study(request):
    return render(request,'dataterminal/study.html')

def entry(request):
    return render(request,'dataterminal/entry.html')    

def plot(request):
    return render(request,'dataterminal/plot.html') 

def obs(request):
    return render(request,'dataterminal/obs.html') 

def qc(request):
    return render(request,'dataterminal/dqc_transaction.html') 
def qc_obs(request):
    return render(request,'dataterminal/qc_obs.html') 

def get_data(request, *args,**kwargs):
    data={
        "FieldMap1":100,
        "FieldMap2":200,
    } 
    return JsonResponse(data)

