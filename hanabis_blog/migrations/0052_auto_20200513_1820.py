# Generated by Django 3.0.5 on 2020-05-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanabis_blog', '0051_auto_20200427_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='date_pub',
            field=models.CharField(auto_created=True, blank=True, default='2020-05-13', max_length=50, null=True, verbose_name='Date'),
        ),
    ]