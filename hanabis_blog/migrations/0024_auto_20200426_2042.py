# Generated by Django 3.0.5 on 2020-04-26 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanabis_blog', '0023_auto_20200426_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='name',
            field=models.CharField(default='Anonymous', max_length=100, null=True, verbose_name='Name'),
        ),
    ]
