# Generated by Django 3.1.14 on 2022-09-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batchrunmodel',
            options={'verbose_name': 'Batch Run'},
        ),
        migrations.AddField(
            model_name='batchrunmodel',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='batchrunmodel',
            name='results',
            field=models.TextField(null=True),
        ),
    ]
