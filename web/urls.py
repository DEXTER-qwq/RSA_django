from django.contrib import admin
from django.urls import path, include
from web.views import index, test, blind

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index, name="index"),
    # 主页面, 显示相关数据
    path('test', test, name="test"),
    path('blind', blind, name="blind")
]
