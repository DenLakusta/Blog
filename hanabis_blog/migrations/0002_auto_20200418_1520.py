# Generated by Django 3.0.5 on 2020-04-18 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hanabis_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(null=True, upload_to='authors_image/', verbose_name='Post image'),
        ),
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=50, verbose_name='Name'), max_length=150, unique=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Draft'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=150, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='post',
            name='auth',
            field=models.ManyToManyField(blank=True, related_name='hanabis_blog', to='hanabis_blog.Author', verbose_name='Authors'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(db_index=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateTimeField(default='', verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='hanabis_blog', to='hanabis_blog.Tag', verbose_name='tags'),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=5000, verbose_name='Message')),
                ('date_pub', models.DateTimeField(blank=True, null=True, verbose_name='Date')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hanabis_blog.Reviews', verbose_name='Parent')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hanabis_blog.Post', verbose_name='post')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]