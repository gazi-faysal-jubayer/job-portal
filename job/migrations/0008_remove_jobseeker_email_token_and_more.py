# Generated by Django 4.1.7 on 2023-04-13 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_remove_recruiter_email_token_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='email_token',
        ),
        migrations.RemoveField(
            model_name='jobseeker',
            name='is_verified',
        ),
    ]
