# Generated by Django 4.0.3 on 2022-05-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_profile_pinterest_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
