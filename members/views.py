from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    all_members = Member.objects.all()
    template = loader.get_template('all_members.html')
    return HttpResponse(template.render({'members': all_members.values()}, request))

def details(request, id):
    member = Member.objects.get(id=id)
    return render(request, 'details.html', {'member': member})
