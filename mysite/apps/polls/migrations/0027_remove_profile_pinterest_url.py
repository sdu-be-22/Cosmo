# Generated by Django 4.0.3 on 2022-05-04 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_profile_linkedin_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='pinterest_url',
        ),
    ]
