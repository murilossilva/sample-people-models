# Generated by Django 3.2.7 on 2021-10-05 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_people_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
