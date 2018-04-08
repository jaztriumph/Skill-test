# Generated by Django 2.0.4 on 2018-04-08 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skillinfo',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='skillinfo',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='skillinfo',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]