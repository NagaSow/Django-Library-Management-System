# Generated by Django 2.1.3 on 2018-11-26 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20181125_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='pic',
        ),
    ]