# Generated by Django 2.2.5 on 2020-02-17 03:32

from django.db import migrations, models
import vishnu.models


class Migration(migrations.Migration):

    dependencies = [
        ('vishnu', '0003_auto_20200211_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='file',
            field=models.ImageField(upload_to=vishnu.models.append_owner_email),
        ),
    ]
