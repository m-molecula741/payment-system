# Generated by Django 3.2.5 on 2021-11-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pay', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USD', models.IntegerField(verbose_name='доллар')),
                ('RUB', models.IntegerField(verbose_name='рубль')),
                ('CNY', models.IntegerField(verbose_name='юань')),
                ('GBP', models.IntegerField(verbose_name='фунты')),
            ],
        ),
    ]
