# Generated by Django 5.1.1 on 2024-09-30 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
    ]
