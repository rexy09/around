# Generated by Django 3.0.2 on 2020-03-05 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200305_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessdetails',
            name='business_category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='businessdetails',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='businessdetails',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='businessdetails',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='businessdetails',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='businessinfo',
            name='birthdate',
            field=models.DateField(),
        ),
    ]