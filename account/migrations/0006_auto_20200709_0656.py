# Generated by Django 3.0.7 on 2020-07-09 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200708_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]