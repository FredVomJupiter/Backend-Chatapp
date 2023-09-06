from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .models import Message, Chat
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if request.method == 'POST':
        print("Received data: " + request.POST['generalmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['generalmessage'], chat=myChat, author=request.user, receiver=request.user)
        chatMessages = Message.objects.filter(chat__id=1)
        return render(request, 'chat/index.html', {'messages': chatMessages})
        logout(request)
        return HttpResponseRedirect('/logout/')
    return render(request, 'chat/index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            print("User logged in")
            return HttpResponseRedirect('/chat/')
    return render(request, 'login/login.html')
        #else:
         #   print("User not logged in")
          #  return render(request, 'login/login.html')
    #else:
     #   return render(request, 'login/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'logout/logout.html')


def register_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('firstPW')
        repeatPassword = request.POST.get('secondPW')
        if password == repeatPassword:
            print("Passwords match")
            print("User registered")
            return HttpResponseRedirect('/login/')
        else:
            print("Passwords do not match")
            return render(request, 'register/register.html')
    return render(request, 'register/register.html')