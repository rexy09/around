# Generated by Django 3.0.7 on 2020-08-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20200823_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcarddetails',
            name='cardholder_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='creditcarddetails',
            name='token',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]