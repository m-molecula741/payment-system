# Generated by Django 3.2.5 on 2021-11-04 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pay', '0002_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.FloatField(verbose_name='баланс'),
        ),
    ]