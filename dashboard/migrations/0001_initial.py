# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-27 16:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('id_no', models.IntegerField(null=True)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('branch', models.CharField(choices=[('ECE', 'Electronics and Communication Engineering'), ('CSE', 'Computer Science & Engineering'), ('MECH', 'Mechanical Engineering'), ('MIN', 'Mining'), ('EEE', 'Electrical and Electronics Engineering'), ('CIV', 'Civil Engineering'), ('CHEM', 'Chemical Engineering'), ('ARCH', 'Architecture'), ('META', 'Metallurgy')], max_length=4)),
                ('enr_no', models.CharField(max_length=11, null=True)),
                ('cgpa', models.FloatField(max_length=5, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('resume', models.FileField(null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Mr', 'Mr.'), ('Ms', 'Ms.'), ('Mrs', 'Mrs.')], max_length=4)),
                ('f_name', models.CharField(max_length=100)),
                ('m_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=4)),
                ('dob', models.DateField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('result', models.CharField(choices=[('NA', 'Has not appeared yet'), ('SE', 'Selected'), ('RJ', 'Rejected')], default='NA', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250)),
                ('company_type', models.CharField(max_length=100)),
                ('req_cgpa', models.FloatField(max_length=5, null=True)),
                ('last_date', models.DateField(null=True)),
                ('salary', models.IntegerField(null=True)),
                ('stipend', models.IntegerField(null=True)),
                ('branch', models.CharField(blank=True, max_length=100)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='applications',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Companies'),
        ),
        migrations.AddField(
            model_name='applications',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
