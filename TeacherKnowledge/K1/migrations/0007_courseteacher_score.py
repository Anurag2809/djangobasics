# Generated by Django 3.0.8 on 2020-08-12 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('K1', '0006_courses_decription'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseteacher',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
