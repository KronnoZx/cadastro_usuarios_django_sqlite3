# Generated by Django 4.2.5 on 2023-09-13 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.TextField(max_length=255)),
                ('nome', models.TextField(max_length=255)),
                ('senha', models.TextField(max_length=255)),
            ],
        ),
    ]
