# Generated by Django 4.1.7 on 2023-04-15 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_remove_jobseeker_email_token_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=13)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]