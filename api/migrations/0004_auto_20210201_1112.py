# Generated by Django 2.2.12 on 2021-02-01 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_userperm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userId',
        ),
        migrations.RemoveField(
            model_name='user',
            name='userPerm',
        ),
    ]
