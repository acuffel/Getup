# Generated by Django 3.0.7 on 2020-07-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200727_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='picture',
            field=models.ImageField(default=None, upload_to='media/images/'),
        ),
    ]
