# Generated by Django 4.0.3 on 2022-05-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_remove_profile_tel_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=150),
        ),
    ]