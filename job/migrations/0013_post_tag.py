# Generated by Django 4.1.7 on 2023-04-15 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(default='', max_length=13),
            preserve_default=False,
        ),
    ]
