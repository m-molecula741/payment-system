# Generated by Django 3.2.5 on 2021-11-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pay', '0003_alter_user_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='CNY',
            field=models.FloatField(verbose_name='юань'),
        ),
        migrations.AlterField(
            model_name='course',
            name='GBP',
            field=models.FloatField(verbose_name='фунты'),
        ),
        migrations.AlterField(
            model_name='course',
            name='RUB',
            field=models.FloatField(verbose_name='рубль'),
        ),
        migrations.AlterField(
            model_name='course',
            name='USD',
            field=models.FloatField(verbose_name='доллар'),
        ),
    ]
