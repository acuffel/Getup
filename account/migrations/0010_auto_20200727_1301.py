# Generated by Django 3.0.7 on 2020-07-27 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20200720_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='picture',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
