# Generated by Django 3.0.2 on 2020-03-13 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_businessdetails_business_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimg',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_pimg', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]