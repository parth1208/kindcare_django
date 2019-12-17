# Generated by Django 2.2.6 on 2019-10-24 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_type', models.CharField(choices=[('sell', 'sell'), ('service', 'service')], max_length=25)),
                ('category_name', models.CharField(max_length=25)),
                ('category_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=25)),
                ('sub_category_desc', models.TextField()),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='seller.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='mi', max_length=25)),
                ('Product_type', models.CharField(max_length=25)),
                ('Product_Price', models.IntegerField()),
                ('Product_Description', models.TextField()),
                ('Product_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('discount', models.FloatField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='seller.Category')),
                ('cat_sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subcategory', to='seller.SubCategory')),
                ('owned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]