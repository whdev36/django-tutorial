from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import ContactForm, MemberCreationForm
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme

def members(request):
    all_members = Member.objects.all()
    print(request.endpoint)
    template = loader.get_template('all_members.html')
    return HttpResponse(template.render({'members': all_members.values()}, request))

def details(request, id):
    member = Member.objects.get(id=id)
    return render(request, 'details.html', {'member': member})

@require_http_methods(["GET", "POST"])
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    username = ''
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        if not username or not password:
            messages.error(request, 'Both username and password are required.', extra_tags='danger')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if not user.is_active:
                    messages.error(request, 'This account is inactive.')
                else:
                    login(request, user)
                    messages.success(request, 'You have successfully logged in.')
                    next_page = request.GET.get('next', getattr(settings, 'LOGIN_REDIRECT_URL', 'home'))
                    return redirect(next_page)
            else:
                messages.error(request, 'Invalid username or password', extra_tags='danger')
    return render(request, 'login.html', {'username': username})

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

@require_http_methods(["GET", "POST"])
def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    next_page = request.GET.get('next', 'home')
    if not url_has_allowed_host_and_scheme(next_page, allowed_hosts={request.get_host()}):
        next_page = 'home'
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to the site.')
            return redirect(next_page)
        else:
            messages.warning(request, 'Please correct the errors below.')
    else:
        form = MemberCreationForm()
    return render(request, 'register.html', {'form': form})