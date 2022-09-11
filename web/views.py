import json

from django.shortcuts import render
from django.http import HttpResponse
import web.RSA_03test as blindSign


# Create your views here.
def init(request):
    # return render(request, "../templates/test.html")
    # e=blindSign.init()[0]
    jsonObj = json.dumps(blindSign.init())
    return HttpResponse(jsonObj)


# def test(request):
#     name = request.GET.get("name")
#     return HttpResponse("Hello " + name)


def blind(request):
    msg = request.GET.get("msg")
    jsonObj = json.dumps(blindSign.blindData(msg))
    # print(request)
    return HttpResponse(jsonObj)


def double_Spending_db(request):
    sigma=request.GET.get('sigma')
    msg=request.GET.get('msg')
    return HttpResponse(blindSign.verify(int(sigma,16),str(msg)))

# def sign(request):
#     msg = request.GET.get("msg")
#     return HttpResponse(str(hex(blindSign.sign(int(msg,16)))))
