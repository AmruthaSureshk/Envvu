# Generated by Django 3.0.8 on 2020-12-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Envvu1', '0006_auto_20201208_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='applynow',
            name='jobtitle',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
