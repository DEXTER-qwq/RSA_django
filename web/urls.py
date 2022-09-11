from django.contrib import admin
from django.urls import path, include
from web.views import init, blind, double_Spending_db

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('init', init, name="init"),
    # 主页面, 显示相关数据
    # path('test', test, name="test"),
    path('blind', blind, name="blind"),  # blind?msg=
    path('verify', double_Spending_db, name="verify"),  # verify?sigma=&msg=
]
