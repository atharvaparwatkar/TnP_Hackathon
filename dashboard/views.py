from django.shortcuts import render, redirect,get_object_or_404
from dashboard.admin import UserChangeForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import MyUser, Companies, Applications
from .admin import EditProfileForm
from datetime import date
from django.core.serializers.json import DjangoJSONEncoder
from django.template.defaultfilters import slugify
import json

@login_required
def dashboard(request):
    # if request.method == 'POST':
    #     if request.user.is_authenticated:
            context = {
                'management_companies': Companies.objects.filter(company_type='Management'),
                'it_companies': Companies.objects.filter(company_type='IT'),
                'core_companies': Companies.objects.filter(company_type='Core'),
                'enr_no'    : request.user.enr_no,
                'id_no'     : request.user.id_no,
                'cgpa'      : request.user.cgpa,
                'branch'    : request.user.branch,
                'full_name' : request.user.full_name,

            }
            return render(request, 'dashboard/index.html', context)
        # else:
            # return HttpResponse('login kar na bhai')
            # return redirect('dashboard:login')
    # else:
    #     return redirect('signup')


def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        user.set_password(password)
        user.save()
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("dashboard:dashboard")
        else:
            return HttpResponse("Some thing was wrong.")
    # else:
    #     return HttpResponse("Form is not valid.")

    return render(request, 'dashboard/signup.html', {"form": form})


def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("dashboard:dashboard")
            else:
                return render(request, 'dashboard/login.html',
                              {'error_message': "This account is disabled. Please contact administration."})
        else:
            return render(request, 'dashboard/login.html',
                          {'error_message': "Invalid Credentials"})
    # else:
    #     return HttpResponse("Form is not valid.")

    return render(request, 'dashboard/login.html', {'WP': 'WP'})

@login_required
def log_out(request):
    logout(request)
    return redirect('home')

@login_required
def edit_prof(request):
    form = EditProfileForm(data=request.POST, instance=request.user)

    msg = "Press 'Save Changes' to make changes."

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.save()
            msg = "Changes Saved."
            # return render(request, 'dashboard/edit_prof.html', {'msg': 'Changes Saved'})

    full_name = request.user.full_name
    enr_no = request.user.enr_no
    id_no = request.user.id_no
    cgpa = request.user.cgpa
    branch = request.user.branch
    email = request.user.email

    # if request.method == "POST":
    #     cgpa = request.POST['cgpa']
    #     MyUser.cgpa = cgpa

    context = {
        'management_companies': Companies.objects.filter(company_type='Management'),
        'it_companies': Companies.objects.filter(company_type='IT'),
        'core_companies': Companies.objects.filter(company_type='Core'),
        'full_name' : full_name,
        'enr_no'    : enr_no,
        'id_no'     : id_no,
        'cgpa'      : cgpa,
        'branch'    : branch,
        'email'     : email,
        'msg'       : msg,
        'form'      : form,
    }
    return render(request, 'dashboard/edit_prof.html', context)


@login_required
def change_pw(request):

    context = {
        'management_companies': Companies.objects.filter(company_type='Management'),
        'it_companies': Companies.objects.filter(company_type='IT'),
        'core_companies': Companies.objects.filter(company_type='Core'),
    }

    if request.method == 'POST':

        old_password = request.POST['old_password']
        user = authenticate(email=request.user.email, password=old_password)
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if user is not None:
            if password1 and password2 and password1 == password2:
                user.set_password(password1)
                user.save()
                return redirect('dashboard:dashboard')

        else:
            msg = 'Wrong old password!'
            return render(request, 'dashboard/change_pw.html', {'msg': msg})

    return render(request, 'dashboard/change_pw.html', context)

@login_required
def app_form(request, company_id):
    if request.method == 'POST':

        application = Applications()
        application.title = request.POST['title']
        application.f_name = request.POST['f_name']
        application.m_name = request.POST['m_name']
        application.l_name = request.POST['l_name']
        application.gender = request.POST['gender']
        application.dob = request.POST['dob']
        application.email = request.POST['email']
        application.mobile = request.POST['mob_no']
        application.address = request.POST['address']
        application.city = request.POST['city']
        application.state = request.POST['state']
        application.country = request.POST['country']
        application.zip = request.POST['zip']

        application.company = Companies.objects.get(pk=company_id)
        application.user = request.user
        application.save()
        return redirect('dashboard:dashboard')

        msg = 'Please enter the same email address used for registration.'

        context = {
            'management_companies': Companies.objects.filter(company_type='Management'),
            'it_companies': Companies.objects.filter(company_type='IT'),
            'core_companies': Companies.objects.filter(company_type='Core'),
            'msg': msg,
        }
        return render(request, 'dashboard/temp.html', context)

    comp = Companies.objects.get(id=company_id)
    try:
        application = Applications.objects.get(company=comp, user=request.user)
        context = {
            'management_companies': Companies.objects.filter(company_type='Management'),
            'it_companies': Companies.objects.filter(company_type='IT'),
            'core_companies': Companies.objects.filter(company_type='Core'),
            'f_name': application.f_name,
        }

        return render(request, 'dashboard/app_form.html', context)

    except Applications.DoesNotExist:
        context = {
            'management_companies': Companies.objects.filter(company_type='Management'),
            'it_companies': Companies.objects.filter(company_type='IT'),
            'core_companies': Companies.objects.filter(company_type='Core'),
        }
        return render(request, 'dashboard/app_form.html', context)
    # if application is not None:
    #     context = {
    #         'management_companies': Companies.objects.filter(company_type='Management'),
    #         'it_companies': Companies.objects.filter(company_type='IT'),
    #         'core_companies': Companies.objects.filter(company_type='Core'),
    #         'f_name': application.f_name,
    #     }


        # return render(request, 'dashboard/app_form.html', context)

    # else:
    #     context = {
    #         'management_companies': Companies.objects.filter(company_type='Management'),
    #         'it_companies': Companies.objects.filter(company_type='IT'),
    #         'core_companies': Companies.objects.filter(company_type='Core'),
    #     }
    #     return render(request, 'dashboard/app_form.html', context)

@login_required
def company_details(request, company_id):

    company = get_object_or_404(Companies, pk=company_id)
    if company is not None:
        data = {}
        data['eligibility'] = company.req_cgpa
        data['salary'] = company.salary
        data['stipend'] = company.stipend
        data['last_date'] = company.last_date
        data['id'] = company.pk

        if request.user.cgpa >= company.req_cgpa:
            data['can_apply'] = 'true'
        else:
            data['can_apply'] = 'false'

        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type="application/json")
        # render_template_to_response("index.html", data)



  #  companyname = get_object_or_404(Companies, company_name=company_name)
  #   company = get_object_or_404(Companies, pk=company_id)
  #   company = Companies.objects.create(company_name=company_name, slug=slugify(company_name))

    # context = {
        # 'management_companies': Companies.objects.filter(company_type='Management'),
        # 'it_companies': Companies.objects.filter(company_type='IT'),
        # 'core_companies': Companies.objects.filter(company_type='Core'),
        #'companyName': companyname,
        # 'company': company,
    # }
    # return render(request, 'dashboard/company_details.html', context)

@login_required
def apply(request):

    if request.method == 'POST':
      #  form = ApplicationForm(request.POST or None)

        application = Applications()
        application.title = request.POST['title']
        application.f_name = request.POST['f_name']
        application.m_name = request.POST['m_name']
        application.l_name = request.POST['l_name']
        application.gender = request.POST['gender']
        application.dob = request.POST['dob']
        application.email = request.POST['email']
        application.mobile = request.POST['mob_no']
        application.address = request.POST['address']
        application.city = request.POST['city']
        application.state = request.POST['state']
        application.country = request.POST['country']
        application.zip = request.POST['zip']

        #application.company = Companies.objects.get(company_name='Google')
        application.user = request.user
        application.save()
        return redirect('dashboard:dashboard')

        # context = {
        #     'management_companies': Companies.objects.filter(company_type='Management'),
        #     'it_companies': Companies.objects.filter(company_type='IT'),
        #     'core_companies': Companies.objects.filter(company_type='Core'),
        #     'msg': msg,
        # }
        # return render(request, 'dashboard/temp.html', context)
    else:
        return render(request, 'dashboard/temp.html')