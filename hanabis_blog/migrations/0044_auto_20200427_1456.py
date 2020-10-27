# Generated by Django 3.0.5 on 2020-04-27 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hanabis_blog', '0043_auto_20200427_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='socialaccount.SocialAccount'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]