# Generated by Django 3.0.8 on 2020-12-07 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Envvu1', '0002_auto_20201207_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='categ',
        ),
        migrations.AddField(
            model_name='blog',
            name='categ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Envvu1.Blogcateg'),
        ),
    ]
