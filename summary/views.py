from django.shortcuts import render
from django.http import HttpResponse
from gensim.summarization import summarize


# Create your views here.

def home(request):
    return render(request,'home.html')

def add(request):

    val1=str(request.GET["num1"])
     
    res =summarize(val1)

    return render(request,"result.html",{"result": res})