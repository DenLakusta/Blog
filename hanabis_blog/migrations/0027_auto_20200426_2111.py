# Generated by Django 3.0.5 on 2020-04-26 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('hanabis_blog', '0026_delete_myusersocial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='name',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='socialaccount.SocialAccount'),
        ),
    ]