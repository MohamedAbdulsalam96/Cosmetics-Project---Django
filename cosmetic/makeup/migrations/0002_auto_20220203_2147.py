# Generated by Django 2.2.18 on 2022-02-03 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]