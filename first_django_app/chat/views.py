from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Message, Chat
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        if Chat.objects.filter(id=request.POST['chatId']).count() > 0:
            myChat = Chat.objects.get(id=request.POST['chatId'])
            Message.objects.create(text=request.POST['message'], chat=myChat, author=request.user, receiver=request.user)
        else: 
            myChat = Chat.objects.create(id=request.POST['chatId'])
            Message.objects.create(text=request.POST['message'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.all()
    return render(request, 'chat/index.html', {'messages': chatMessages})


#print("Received data: " + request.POST['generalmessage'])
 #       if Chat.objects.filter(id=1).count() > 0:
  #          myChat = Chat.objects.get(id=1)
   #         Message.objects.create(text=request.POST['generalmessage'], chat=myChat, author=request.user, receiver=request.user)
    #    else: 
     #       myChat = Chat.objects.create(id=1)
      #      Message.objects.create(text=request.POST['generalmessage'], chat=myChat, author=request.user, receiver=request.user)
       # #chatMessages = Message.objects.filter(chat__id=1)
        #return render(request, 'chat/index.html', {'messages': chatMessages})



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


def logout_view(request):
    logout(request)
    return render(request, 'logout/logout.html')


def register_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful." )
            return HttpResponseRedirect('/login/')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            return render(request, 'register/register.html')
    form = NewUserForm()
    return render(request, 'register/register.html')


def redirect_view(request):
    return HttpResponseRedirect('/login/')