# Generated by Django 4.0.2 on 2022-02-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_rename_city_ninja_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='jsh'),
        ),
    ]
