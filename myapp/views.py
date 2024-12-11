from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context={
        'name': 'Anku',
        'age': 18,
        'nationality': 'India'
    }
    return render(request,'index.html',context)
def counter(request):
    words=request.POST['words']
    nWords=len(words.split())
    context={
        'nWords':nWords
    }
    return render(request,'counter.html',context)
# Create your views here.
