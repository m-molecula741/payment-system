from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from json import *
import json
from django.http import HttpResponse, JsonResponse

from django.db import connection
from .models import User,Course


class ShowBalance(APIView):
    """ Просмотр баланса"""
    def get(self, request):
        pers_id = request.GET.get('id')
        person = User.objects.get(id=pers_id)
        bal = person.balance

        bound = {
            'user_name' : person.user_name,
            'balance in EUR' : bal
        }


        return JsonResponse(bound)


class ChangeBalance(APIView):
    """Пополнение баланса"""
    def get(self, request):
        pers_id = request.GET.get('id')
        pers_balance= request.GET.get('balance')
        operation = request.GET.get('operation')

        if float(pers_balance) < 0:
            resp = {
                'err': 'the value is negative'
            }
            return JsonResponse(resp)

        user = User.objects.get(id=pers_id)
        bal = user.balance

        if operation == 'add':
            person = User.objects.filter(id=pers_id).update(balance=bal + float(pers_balance))

            resp = {
                "balance increased by" : pers_balance
            }

        elif operation == 'decrease':
            if bal - float(pers_balance) >= 0:
                person = User.objects.filter(id=pers_id).update(balance=bal - float(pers_balance))

                resp = {
                    "balance reduced by": pers_balance
                }

            else:

                resp = {
                    'error': 'not enough money in the account'
                }

        else:

            resp = {
                'err': 'this operation does not exist'
            }

        return JsonResponse(resp)


class MoneyTransfer(APIView):
    """Перевод денег"""
    def get(self, request):
        pers1_id = request.GET.get('id1')
        pers2_id = request.GET.get('id2')
        amount = request.GET.get('amount')

        if float(amount) <= 0:

            am_er = {
                'err': 'transfer to a positive amount of money is not possible'
            }

            return JsonResponse(am_er)

        user = User.objects.get(id=pers1_id)
        bal = user.balance
        if bal - float(amount) >= 0:
            person = User.objects.filter(id=pers1_id).update(balance=bal - float(amount))

            user2 = User.objects.get(id=pers2_id)
            bal2 = user2.balance
            person = User.objects.filter(id=pers2_id).update(balance=bal2 + float(amount))

            resp = {
                "translation_status" : "ok"
            }

        else:

            resp = {
                'err': 'there is not enough money on the balance'
            }

        return JsonResponse(resp)


class Converter(APIView):
    """Конвертер валют"""
    def get(self, request):
        response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=aa88959d60ddced0ce07e04098be8bcd').json()
        pers_id = request.GET.get('id')
        currency = request.GET.get('currency')
        person = User.objects.get(id=pers_id)
        bal = person.balance

        if response:
            if currency in response['rates']:
                balance = bal * float(response['rates'][currency])

                bound = {
                    'user_name': person.user_name,
                    currency: balance
                }

            else:

                bound = {
                    'err': 'this currency does not exist'
                }

        else:
            course_val = Course.objects.latest("id")
            if currency == 'RUB':
                value = course_val.RUB
            elif currency == 'USD':
                value = course_val.USD
            elif currency == 'CNY':
                value = course_val.CNY
            elif currency == 'GBP':
                value = course_val.GBP
            else:
                err = {
                    'error': 'this currency does not exist'
                }
                return JsonResponse(err)

            balance = bal * value

            bound = {
                'user_name': person.user_name,
                currency: balance
            }

        return JsonResponse(bound)








