# Generated by Django 3.0.2 on 2020-02-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessdetails',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='businessdetails',
            name='directions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
