# Generated by Django 4.0.3 on 2022-05-06 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0029_remove_comment_name_comment_user_alter_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='body',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.CharField(default='', max_length=255),
        ),
    ]