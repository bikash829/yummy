# Generated by Django 5.0 on 2024-01-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section_content', '0007_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='guests',
            field=models.IntegerField(default=0),
        ),
    ]
