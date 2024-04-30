# Generated by Django 5.0.4 on 2024-04-27 07:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='travelblog.country')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('duration', models.DurationField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('location', models.CharField(max_length=200)),
                ('suitability', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='activities_images/')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelblog.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelblog.country')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('summary', models.TextField()),
                ('content', models.TextField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='posts_images/')),
                ('location', models.CharField(max_length=200)),
                ('tags', models.CharField(blank=True, max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelblog.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelblog.country')),
            ],
        ),
    ]