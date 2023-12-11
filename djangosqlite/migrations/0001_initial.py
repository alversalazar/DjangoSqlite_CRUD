# Generated by Django 4.2.7 on 2023-11-26 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('status', models.BooleanField(null=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('modifieddate', models.DateTimeField(auto_now=True)),
                ('idUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'carrer',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('socialsegurity', models.CharField(max_length=11)),
                ('dateofhire', models.DateTimeField()),
                ('status', models.BooleanField(null=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('modifieddate', models.DateTimeField(auto_now=True)),
                ('idUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'employee',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Viatic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status', models.BooleanField(null=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('modifieddate', models.DateTimeField(auto_now=True)),
                ('idEmployee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangosqlite.employee')),
                ('idUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'viatic',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('credit', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('characteristic', models.CharField(max_length=50)),
                ('keymatter', models.CharField(max_length=50)),
                ('status', models.BooleanField(null=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('modifieddate', models.DateTimeField(auto_now=True)),
                ('idUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'subject',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Studyplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objetive', models.CharField(max_length=100)),
                ('datestart', models.DateTimeField()),
                ('datefinal', models.DateTimeField()),
                ('key', models.CharField(max_length=20)),
                ('status', models.BooleanField(null=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('modifieddate', models.DateTimeField(auto_now=True)),
                ('idCarrer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangosqlite.carrer')),
                ('idUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'studyplan',
                'ordering': ['id'],
            },
        ),
    ]
