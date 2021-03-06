# Generated by Django 2.2.6 on 2019-12-20 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ser', '0008_service_categary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=25)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Services', to='ser.Service_Categary')),
            ],
        ),
    ]
