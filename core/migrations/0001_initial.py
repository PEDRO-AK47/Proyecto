# Generated by Django 5.0.1 on 2024-06-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(max_length=2, primary_key=True, serialize=False)),
                ('nombre_p', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
                ('info', models.CharField(max_length=100)),
            ],
        ),
    ]
