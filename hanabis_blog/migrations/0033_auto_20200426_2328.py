# Generated by Django 3.0.5 on 2020-04-26 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanabis_blog', '0032_auto_20200426_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='username',
            field=models.CharField(max_length=100, null=True, verbose_name='username'),
        ),
    ]
