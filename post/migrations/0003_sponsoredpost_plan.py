# Generated by Django 3.0.7 on 2020-07-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_sponsoredpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsoredpost',
            name='plan',
            field=models.PositiveIntegerField(choices=[(7, '7 Days'), (30, '30 Days'), (60, '3 Months'), (120, '6 Months'), (366, '1 Year')], default=0),
        ),
    ]
