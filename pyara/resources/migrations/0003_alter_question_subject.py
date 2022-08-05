# Generated by Django 3.2.5 on 2022-08-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_question_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.CharField(choices=[('GEN', 'General information'), ('BAS', 'Basic data types and syntax'), ('COL', 'Built-in data types used to store collections of data'), ('FUN', 'Functions'), ('OOP', 'Object Oriented Programming'), ('FIL', 'Files handling'), ('ALG', 'Algorithms')], default='GEN', max_length=3),
        ),
    ]