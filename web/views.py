import json
from django.shortcuts import render
from django.http import HttpResponse
import web.RSA_03test as blindSign
from web.models import SpendingInfo, Message, User


# Create your views here.
def init(request):
    # return render(request, "../templates/test.html")
    # e=blindSign.init()[0]
    jsonObj = json.dumps(blindSign.init())
    return HttpResponse(jsonObj)


def blind(request):
    msg = request.GET.get("msg")
    jsonObj = json.dumps(blindSign.blindData(msg))
    # print(request)
    return HttpResponse(jsonObj)


def double(request):
    sigma = request.GET.get('sigma')
    msg = request.GET.get('msg')
    try:
        mod = SpendingInfo.objects  # 获取SpendingInfo模型的Model操作对象
        spending = mod.get(sigma=sigma, msg=msg)
        spending.__dict__.pop("_state")
        print(spending.__dict__)
        return HttpResponse("双花")
    except:
        if (blindSign.verify(int(sigma, 16), str(msg))):
            ob = SpendingInfo()
            ob.sigma = sigma
            ob.msg = msg
            ob.save()
            return HttpResponse('valid')
        else:
            return HttpResponse('invalid')


def pay(request):
    payer = request.GET.get("payer")
    payee = request.GET.get("payee")
    msg = request.GET.get("msg")
    money = request.GET.get("money")
    for i in range(0, int(money)):
        ob = Message()
        ob.payer = payer
        ob.payee = payee
        ob.msg = msg+str(i)
        ob.sigma = blindSign.payData(msg+str(i))
        ob.save()
        print('1')
    # jsonObj = json.dumps(blindSign.payData(payer, payee, msg))
    # return HttpResponse(jsonObj)
    print('2')
    return HttpResponse('end')


def getUser(request):
    pass
