from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Transfer
# Create your views here.
def home(request):
    return render(request, 'home.html')
def user_register(request):
    context = {}
    form = UserCreationForm()
    context['form'] = form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('<p>Error saving user</p>')
    return render(request, 'register.html', context)

def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('<p>No user found</p>')
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def upload_file(request):
    if request.method == 'POST':
        curr = request.user
        sender = curr
        reciever_username = request.POST['sendername']
        reciever = User.objects.get(username=reciever_username)
        file = request.FILES['file']
        filename = file.name
        transfer_instance = Transfer(sender=sender, reciever=reciever, file=file, filename=filename)
        transfer_instance.save()
        return redirect('home')
    return render(request, 'upload_file.html')

def sent_files(request):
    context = {}
    curr = request.user
    if curr.is_authenticated:
        all_files = Transfer.objects.filter(sender=curr)
        context['all_files'] = all_files
    return render(request, 'sent_file_list.html', context)

def recieved_files(request):
    context = {}
    curr = request.user
    if curr.is_authenticated:
        all_files = Transfer.objects.filter(reciever=curr)
        context['all_files'] = all_files
    return render(request, 'recieved_file_list.html', context)

def download_file(request, filename):
    file_dets = Transfer.objects.get(filename=filename)
    context={}
    context['file_url'] = file_dets.file.url
    return render(request,'download.html', context)