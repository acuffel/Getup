# Generated by Django 3.0.7 on 2020-07-09 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_customuser_re_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='re_email',
        ),
    ]
