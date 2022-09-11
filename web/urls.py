from django.contrib import admin
from django.urls import path, include
from web.views import init, blind,double

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('init', init, name="init"),
    # 主页面, 显示相关数据
    path('blind', blind, name="blind"),  # blind?msg=
    path('double', double, name="double"),  # double?sigma=&msg
]
