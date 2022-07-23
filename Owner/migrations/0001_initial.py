# Generated by Django 3.0.4 on 2020-12-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Owner_firstname', models.CharField(max_length=60)),
                ('Owner_lastname', models.CharField(max_length=60)),
                ('Owner_address', models.CharField(max_length=600)),
                ('Owner_email', models.CharField(max_length=100)),
                ('Owner_dob', models.DateField()),
                ('Owner_mobileno', models.CharField(max_length=10)),
                ('Owner_age', models.IntegerField(max_length=3)),
                ('Owner_license', models.CharField(max_length=600)),
                ('Owner_agency', models.CharField(max_length=100)),
            ],
        ),
    ]