# Generated by Django 4.1.7 on 2023-05-01 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoinformation',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
