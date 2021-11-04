from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('show', views.ShowBalance.as_view()),
    path('change', views.ChangeBalance.as_view()),
    path('translation', views.MoneyTransfer.as_view()),
    path('converter', views.Converter.as_view()),
]