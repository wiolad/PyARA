# Generated by Django 3.2.5 on 2022-11-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0012_answer_drawing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='drawing',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
