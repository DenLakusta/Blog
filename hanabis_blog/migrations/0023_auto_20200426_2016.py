# Generated by Django 3.0.5 on 2020-04-26 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('hanabis_blog', '0022_auto_20200426_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='name',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='socialaccount.SocialAccount'),
        ),
    ]
