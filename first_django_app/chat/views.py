from django.shortcuts import render
from .models import Message, Chat
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if request.method == 'POST' and request.POST['logout'] == 'logout':
        logout(request)
        return render(request, 'logout/logout.html')
    if request.method == 'POST':
        print("Received data: " + request.POST['generalmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['generalmessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})


def login_check(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("User logged in")
            return render(request, 'chat/index.html')
        else:
            print("User not logged in")
            return render(request, 'login/login.html')
    else:
        return render(request, 'login/login.html')