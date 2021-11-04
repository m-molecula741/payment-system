from django.db import models

class User(models.Model):
    """Юзеры"""
    user_name = models.CharField("ник", max_length=40)
    balance = models.FloatField("баланс")


class Course(models.Model):
    """Курсы валют"""
    USD = models.FloatField("доллар")
    RUB = models.FloatField("рубль")
    CNY = models.FloatField("юань")
    GBP = models.FloatField("фунты")
