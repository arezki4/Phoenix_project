# Generated by Django 4.2.8 on 2023-12-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_mentalbase_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentalbase',
            name='lastname',
            field=models.CharField(max_length=15, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='mentalbase',
            name='surname',
            field=models.CharField(max_length=15, verbose_name='Prénom'),
        ),
    ]
