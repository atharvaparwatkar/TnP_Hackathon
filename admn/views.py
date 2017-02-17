from django.shortcuts import render
from dashboard.models import Companies,MyUser,Applications
from django.shortcuts import render, redirect,get_object_or_404
from dashboard.admin import UserChangeForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from dashboard.admin import EditProfileForm
from datetime import date
from django.core.serializers.json import DjangoJSONEncoder
from django.template.defaultfilters import slugify
import json

# @login_required
def applications(request):

    if 'query' in request.GET:
        application = Applications.objects.filter(company__company_name__contains=request.GET['query'])
    else:
        application = Applications.objects.all()
    return render(request, 'admn/applications_page.html', {'application': application})




