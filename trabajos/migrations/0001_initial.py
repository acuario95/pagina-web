# Generated by Django 4.2 on 2024-07-15 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('liga', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]
