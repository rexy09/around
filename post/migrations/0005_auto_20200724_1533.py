# Generated by Django 3.0.7 on 2020-07-24 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200723_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsoredpost',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sponsored_post', to='post.Post'),
        ),
    ]
