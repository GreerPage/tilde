# Generated by Django 3.0.3 on 2020-03-12 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200311_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='imgupload',
            name='h',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='imgupload',
            name='w',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='imgupload',
            name='x',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='imgupload',
            name='y',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
