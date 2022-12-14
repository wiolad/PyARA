# Generated by Django 3.2.5 on 2022-08-02 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.CharField(choices=[('GEN', 'General'), ('LIS', 'Lists'), ('DIC', 'Dictionaries'), ('STR', 'Strings'), ('TUP', 'Tuples'), ('SET', 'Sets'), ('FUN', 'Functions'), ('OOP', 'Object Oriented Programming'), ('FIL', 'Files handling'), ('ALG', 'Algorithms')], default='GEN', max_length=3),
        ),
    ]
