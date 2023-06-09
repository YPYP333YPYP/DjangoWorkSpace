# Generated by Django 4.1.7 on 2023-05-03 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmap', '0004_centerlist_dispatchlist_orderlist_vehiclelist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centerlist',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='centerlist',
            name='longitude',
        ),
        migrations.AddField(
            model_name='centerlist',
            name='geo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tmap.geoinformation'),
        ),
    ]
