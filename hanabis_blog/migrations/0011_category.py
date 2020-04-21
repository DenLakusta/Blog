# Generated by Django 3.0.5 on 2020-04-20 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanabis_blog', '0010_auto_20200420_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Tag')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]