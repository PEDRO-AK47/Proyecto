# Generated by Django 5.0.6 on 2024-07-02 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='info',
            field=models.CharField(max_length=400),
        ),
    ]
