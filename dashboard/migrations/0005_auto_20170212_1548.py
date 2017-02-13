# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-12 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20170212_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='title',
            field=models.CharField(choices=[('Ms', 'Ms.'), ('Mr', 'Mr.'), ('Mrs', 'Mrs.')], max_length=4),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='branch',
            field=models.CharField(choices=[('MIN', 'Mining'), ('META', 'Metallurgy'), ('CSE', 'Computer Science & Engineering'), ('CHEM', 'Chemical Engineering'), ('MECH', 'Mechanical Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('CIV', 'Civil Engineering'), ('ARCH', 'Architecture')], max_length=4),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='enr_no',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='id_no',
            field=models.IntegerField(null=True),
        ),
    ]