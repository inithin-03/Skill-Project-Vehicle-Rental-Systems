# Generated by Django 3.0.4 on 2020-12-21 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerHome', '0002_auto_20201221_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_gender',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]