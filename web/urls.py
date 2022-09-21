from django.contrib import admin
from django.urls import path, include
# from web.views import init, blind,double, pay,getUser,getMessage,newCurrency,delCurrency,showCurrency
from web.views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('init', init, name="init"),
    # 主页面, 显示相关数据
    path('blind', blind, name="blind"),  # blind?msg=
    path('double', double, name="double"),  # double?sigma=&msg
    path('pay', pay, name="pay"),  # pay?payer=&payee=&msg
    path('getUser', getUser, name="getUser"), # getUser
    path('getMessage', getMessage, name="getMessage"),  # getMessage
    path('newCurrency', newCurrency, name="newCurrency"),  # newCurrency
    path('delCurrency', delCurrency, name="delCurrency"),  # delCurrency
    path('showCurrency', showCurrency, name="showCurrency"),  # delCurrency
    path('readCurrency',readCurrency,name="readCurrency"), # readCurrency
    path('userPay', userPay, name="userPay"),  # userPay?payer=&payee=&msg
]
