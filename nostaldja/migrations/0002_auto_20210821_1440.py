# Generated by Django 3.2.6 on 2021-08-21 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decade',
            name='start_year',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='fad',
            name='description',
            field=models.TextField(default='blank'),
        ),
    ]
