# Generated by Django 4.2.1 on 2023-06-03 16:32

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Suelo', models.CharField(max_length=45)),
                ('Cantidad', models.IntegerField()),
                ('Descripcion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('groups', models.ManyToManyField(related_name='custom_users', related_query_name='custom_user', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='custom_users', related_query_name='custom_user', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Producto', models.CharField(max_length=45)),
                ('Descripcion', models.CharField(max_length=45)),
                ('Stock', models.IntegerField()),
                ('Precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=45)),
                ('Cant_participante', models.IntegerField()),
                ('Descripcion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.IntegerField()),
                ('Productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportHub.productos')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportHub.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Reservaciones_Cancha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Horarios', models.DateField()),
                ('Cancha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportHub.cancha')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportHub.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomYApell', models.CharField(max_length=30)),
                ('Domicilio', models.CharField(max_length=30)),
                ('DNI', models.IntegerField()),
                ('Telefono', models.IntegerField()),
                ('Fecha_Nac', models.DateField()),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportHub.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nivel_Tenis', models.CharField(max_length=10)),
                ('Desafio', models.BooleanField()),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportHub.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mymodels', to='SportHub.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportHub.torneo')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportHub.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo_Factura', models.IntegerField()),
                ('Ventas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportHub.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Canchas_Torneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Canchas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportHub.cancha')),
                ('Torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportHub.torneo')),
            ],
        ),
    ]