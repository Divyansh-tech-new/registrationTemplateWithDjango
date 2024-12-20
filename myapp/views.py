from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User,auth
from django.contrib import messages

def index(request):
    features = Feature.objects.all()
    context = {
        'name': 'Anku',
        'age': 18,
        'nationality': 'India',
        'features': features
    }
    return render(request, 'index.html', context)

def counter(request):
    posts=[1,2,3,4,5,'tim','tom','john']
    # words = request.POST['words']
    # nWords = len(words.split())
    # context = {
    #     'nWords': nWords
    # }
    return render(request, 'counter.html', {'posts':posts})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful! Please log in.')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    
    return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
    else:    
        return render (request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request,'post.html',{'pk':pk})