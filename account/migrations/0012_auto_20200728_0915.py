# Generated by Django 3.0.7 on 2020-07-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200728_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='picture',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
