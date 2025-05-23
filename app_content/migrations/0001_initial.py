# Generated by Django 5.0 on 2023-12-19 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tab_name', models.CharField(max_length=100)),
                ('active_status', models.BooleanField(default=False)),
                ('tab_id', models.CharField(blank=True, max_length=100, unique=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100)),
                ('section_title', models.CharField(blank=True, max_length=100)),
                ('section_background_photo', models.ImageField(blank=True, max_length=191, upload_to='static/img/section_background/')),
                ('bg_color', models.CharField(blank=True, max_length=20)),
                ('notes', models.TextField(blank=True)),
                ('site_menu', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_content.sitemenu')),
            ],
        ),
    ]
