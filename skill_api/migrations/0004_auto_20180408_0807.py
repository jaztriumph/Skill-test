# Generated by Django 2.0.4 on 2018-04-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_api', '0003_remove_skillinfo_rejected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillinfo',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]