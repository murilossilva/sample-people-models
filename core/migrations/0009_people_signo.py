# Generated by Django 3.2.7 on 2021-10-05 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_people_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='signo',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
