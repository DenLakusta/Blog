# Generated by Django 3.0.5 on 2020-04-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanabis_blog', '0005_auto_20200418_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='auth',
            field=models.ManyToManyField(blank=True, related_name='hanabis_blog', to='hanabis_blog.Author', verbose_name='Authors'),
        ),
    ]
