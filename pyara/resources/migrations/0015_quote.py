# Generated by Django 3.2.5 on 2022-11-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0014_auto_20221118_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, unique=True)),
                ('en', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
