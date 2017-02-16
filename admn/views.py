from django.shortcuts import render
from django.shortcuts import redirect
from dashboard.models import Companies
from .admin import CompanyCreationForm, CompanyChangeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def companies(request):
    # compaies = Companies.objects.values('company_name', 'id', 'applications__user__applications').order_by('-id')

    if 'query' in request.GET:
        compaies = Companies.objects.filter(company_name__contains=request.GET['query']).order_by('-id')
    else:
        compaies = Companies.objects.all().order_by('-id')
    return render(request, 'admn/company_list.html', {'companies': compaies})

Company_Type = [
    'IT',
    'Core',
    'Management',
]

@login_required
def add_company(request):
    form = CompanyCreationForm(data=request.POST)

    # msg = "Press 'Save Changes' to make changes."

    if request.method == 'POST':
        if form.is_valid():
            company = form.save()
            company.save()
            # msg = "Changes Saved."
            # return render(request, 'dashboard/edit_prof.html', {'msg': 'Changes Saved'})
            # return redirect('admn:companies')
            return redirect('admn:companies')
        else:
            return HttpResponse('form not valid')

    return render(request, 'admn/new_company.html')


@login_required
def edit_company(request, company_id):
    form = CompanyChangeForm(data=request.POST, instance=Companies.objects.get(pk=company_id))

    # msg = "Press 'Save Changes' to make changes."

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.save()
            msg = "Changes Saved."
            return render(request, 'admn/edit_company.html', {'msg': 'Changes Saved'})

    company = Companies.objects.get(pk=company_id)
    company.last_date = company.last_date.strftime('%Y-%m-%d')

    context = {
        'company': company,
        # 'msg'       : msg,
        'form'      : form,
    }
    return render(request, 'admn/edit_company.html', context)
