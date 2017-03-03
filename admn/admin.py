from django.contrib import admin
from django import forms
from dashboard.models import Companies, Applications


class CompanyCreationForm(forms.ModelForm):

    class Meta:
        model = Companies
        fields = ('company_name', 'company_type', 'req_cgpa', 'last_date', 'salary', 'stipend', 'branch',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        company = super(CompanyCreationForm, self).save(commit=False)
        if commit:
            company.save()
        return company


class CompanyChangeForm(forms.ModelForm):

    class Meta:
        model = Companies
        fields = ('company_name', 'company_type', 'req_cgpa', 'last_date', 'salary', 'stipend', 'branch',)


class EditApplication(forms.ModelForm):

    class Meta:
        model = Applications
        fields = ('result', 'title')
