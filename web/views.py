import json
from django.shortcuts import render
from django.http import HttpResponse
import web.RSA_03test as blindSign
from web.models import SpendingInfo


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


# def double_Spending_db(request):
#     sigma=request.GET.get('sigma')
#     msg=request.GET.get('msg')
#     return HttpResponse(blindSign.verify(int(sigma,16),str(msg)))

# def sign(request):
#     msg = request.GET.get("msg")
#     return HttpResponse(str(hex(blindSign.sign(int(msg,16)))))

# def test(request):
#     mod = SpendingInfo.objects #获取SpendingInfo模型的Model操作对象
#     ulist = mod.filter("id")[:3]
#     for u in ulist:
#         print(u.id,u.sigma,u.msg)
#         u.__dict__.pop("_state")
#         print(u.__dict__)
#     return HttpResponse(u.__dict__)

def double(request):
    sigma=request.GET.get('sigma')
    msg=request.GET.get('msg')
    try:
        mod = SpendingInfo.objects #获取SpendingInfo模型的Model操作对象
        spending=mod.get(sigma=sigma,msg=msg)
        # for s in spending:
        #     s.__dict__.pop("_state")
        #     print(s.__dict__)
        #     if(s.__dict__):
        #         return HttpResponse("双花")
        spending.__dict__.pop("_state")
        print(spending.__dict__)
        return HttpResponse("双花")
    except:
        if(blindSign.verify(int(sigma,16),str(msg))):
            ob=SpendingInfo()
            ob.sigma=sigma
            ob.msg=msg
            ob.save()
            return HttpResponse('valid')
        else:
            return HttpResponse('invalid')