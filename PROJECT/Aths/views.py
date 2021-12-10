from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def OHM(request):
    return HttpResponse('PLEASE WAIT')

def HOME(request):
    return render(request,'Aths/home.html')
