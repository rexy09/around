# Generated by Django 3.0.7 on 2020-07-23 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_sponsoredpost_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsoredpost',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sponsored', to='post.Post'),
        ),
    ]
