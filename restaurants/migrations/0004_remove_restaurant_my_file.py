# Generated by Django 2.1.5 on 2019-02-14 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20190214_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='my_file',
        ),
    ]
