# Generated by Django 2.2.6 on 2020-02-08 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ser', '0014_auto_20200208_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='servant',
            name='image',
            field=models.ImageField(null=True, upload_to='Worker Image'),
        ),
        migrations.AddField(
            model_name='servant',
            name='phone',
            field=models.BigIntegerField(default=0),
        ),
    ]
