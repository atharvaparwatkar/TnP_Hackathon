# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-27 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='result',
            field=models.CharField(choices=[('RJ', 'Rejected'), ('SE', 'Selected'), ('NA', 'Has not appeared yet')], default='NA', max_length=5),
        ),
        migrations.AlterField(
            model_name='applications',
            name='title',
            field=models.CharField(choices=[('Mr', 'Mr.'), ('Mrs', 'Mrs.'), ('Ms', 'Ms.')], max_length=4),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='branch',
            field=models.CharField(choices=[('CIV', 'Civil Engineering'), ('META', 'Metallurgy'), ('ARCH', 'Architecture'), ('MECH', 'Mechanical Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('CHEM', 'Chemical Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('CSE', 'Computer Science & Engineering'), ('MIN', 'Mining')], max_length=4),
        ),
    ]
