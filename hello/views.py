from django.shortcuts import render
import numpy as np
from celery import Celery, Task
# Create your views here.
from django.http import HttpResponse


def home(request):
    s=1+2
    b="s"
    result=str(s)+b
    a = np.array([1, 2, 3, 4, 5])
    print("1D array:")
    print(a)
    a=cal(100)
    a=str(a)
    data=np.array([1, 2, 3, 4, 5])
    # return HttpResponse("Hello, Django!"+result+a)
    return render(request,"home.html",{"data":data})


def cal(a):
    output=a**2
    return output


def test(request):
    a=1

def card(request):
    data=['a','b','c']
    #data=np.array([1, 2, 3, 4, 5])
    return render(request, 'card.html',{"words":data})