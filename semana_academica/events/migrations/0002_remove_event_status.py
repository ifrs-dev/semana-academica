# Generated by Django 2.1.2 on 2018-10-22 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='status',
        ),
    ]
