# Generated by Django 4.2.2 on 2023-06-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metodo_de_pago', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
