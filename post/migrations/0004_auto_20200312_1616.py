# Generated by Django 3.0.3 on 2020-03-12 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200311_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imgupload',
            name='h',
        ),
        migrations.RemoveField(
            model_name='imgupload',
            name='w',
        ),
        migrations.RemoveField(
            model_name='imgupload',
            name='x',
        ),
        migrations.RemoveField(
            model_name='imgupload',
            name='y',
        ),
    ]