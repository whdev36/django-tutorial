from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import ContactForm

def members(request):
    all_members = Member.objects.all()
    template = loader.get_template('all_members.html')
    return HttpResponse(template.render({'members': all_members.values()}, request))

def details(request, id):
    member = Member.objects.get(id=id)
    return render(request, 'details.html', {'member': member})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}!')
            return redirect('home')
        else:
            messages.warning(request, 'Account does not exist, please log in.')
    return render(request, 'login.html', {})


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
    else:
        form = ContactForm()
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({'form': form}, request))
