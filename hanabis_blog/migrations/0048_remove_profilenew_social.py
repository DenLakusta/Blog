# Generated by Django 3.0.5 on 2020-04-27 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hanabis_blog', '0047_auto_20200427_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilenew',
            name='social',
        ),
    ]
