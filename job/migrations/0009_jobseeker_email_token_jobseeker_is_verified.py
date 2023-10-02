# Generated by Django 4.1.7 on 2023-04-13 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_remove_jobseeker_email_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='email_token',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
