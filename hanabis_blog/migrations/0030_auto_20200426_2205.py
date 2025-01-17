# Generated by Django 3.0.5 on 2020-04-26 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hanabis_blog', '0029_auto_20200426_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True, verbose_name='Email'),
        ),
    ]
