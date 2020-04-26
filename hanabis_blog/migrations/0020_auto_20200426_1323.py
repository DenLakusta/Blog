# Generated by Django 3.0.5 on 2020-04-26 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('hanabis_blog', '0019_auto_20200425_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('avatar_url', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
        migrations.AlterField(
            model_name='reviews',
            name='date_pub',
            field=models.CharField(auto_created=True, blank=True, default='2020-04-26', max_length=50, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='email',
            field=models.EmailField(blank=True, default='anonymous@gmail.com', max_length=150, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='name',
            field=models.CharField(default='Anonymous', max_length=100, null=True, verbose_name='Name'),
        ),
    ]
