# Generated by Django 5.0.2 on 2024-05-20 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='department',
            field=models.CharField(default='empty', max_length=500),
        ),
    ]
