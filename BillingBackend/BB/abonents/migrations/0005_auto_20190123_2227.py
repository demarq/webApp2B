# Generated by Django 2.1.5 on 2019-01-23 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abonents', '0004_auto_20190123_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariffs',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
