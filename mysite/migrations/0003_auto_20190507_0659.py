# Generated by Django 2.2 on 2019-05-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20190429_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='del_pass',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
