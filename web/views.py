import json
# import org.json.JSONObject
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import web.RSA_03test as blindSign
from web.models import SpendingInfo, Message, User, Cryptocurrency


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
    # payer = request.GET.get("payer")
    # payee = request.GET.get("payee")
    msg = request.GET.get("msg")
    money = request.GET.get("money")
    for i in range(0, int(money)):
        ob = Message()
        # ob.payer = payer
        # ob.payee = payee
        ob.msg = msg + str(i)
        ob.sigma = blindSign.payData(msg + str(i))
        ob.save()
        print('1')
    # jsonObj = json.dumps(blindSign.payData(payer, payee, msg))
    # return HttpResponse(jsonObj)
    print('2')
    return HttpResponse('end')


def getUser(request):
    user = User.objects
    # print(user.values())
    # print(user.values()[0])
    print(list(user.values()))
    # 转换类型为list, 方便jsonRes返回json数组
    return JsonResponse(list(user.values()), safe=False)


def getMessage(request):
    message = Message.objects.order_by("-id")[:10]
    print(list(message.values()))
    return JsonResponse(list(message.values()), safe=False)


def newCurrency(request):
    value = request.GET.get("value")
    key = blindSign.cryptocurrencyAdd()
    ob = Cryptocurrency()
    ob.n = key[0]
    ob.e = key[1]
    ob.d = key[2]
    ob.value = value
    ob.save()
    return HttpResponse("1")


def delCurrency(request):
    value = request.GET.get("value")
    ob = Cryptocurrency.objects
    currency = ob.get(value=value).delete()
    return HttpResponse(currency)


def showCurrency(request):
    ob = Cryptocurrency.objects.order_by("value")
    print(list(ob.values()))
    return JsonResponse(list(ob.values()), safe=False)


def userPay(request):
    payer = request.GET.get("payer")
    msg = request.GET.get("msg")
    money = request.GET.get("money")
    # try:
    ob = User.objects
    payer = ob.get(name=payer)
    # print(payer)
    # print(type(payer.money))
    # print(type(int(money)))
    if payer.money > int(money):
        payer.money = payer.money - int(money)
        payer.save()
        # TODO 加密json数组
        list = blindSign.decompose(int(money), readCurrency())
        print(list)
        # returnCurrency(msg,list)
        return JsonResponse(returnCurrency(msg,list),safe=False)
    else:
        return HttpResponse("1")
    # except:
    #     return HttpResponse("false")


def readCurrency():
    ob = Cryptocurrency.objects.order_by("-value")
    print(list(ob.values()))
    print(len(list(ob.values())))
    print(list(ob.values())[0])

    # print(ob.values_list("value"))
    value = []
    for i in list(ob.values()):
        value.append(i["value"])
        # print(i["value"])
    print(value)
    # 获得有序数组
    return value


def returnCurrency(msg, currencyList):
    ob = Cryptocurrency.objects.order_by("-value")
    value = []
    data={
        'sigma':'',
        'msg':'',
    }
    tmp={
        'sigma':'',
        'msg':'',
    }
    # for i in list(ob.values()):
    #     for j in currencyList:
    #         msg=msg+str(j)
    #         blindSign.payData(msg,i["n"],i["e"],i["d"])
    for i in range(0, len(list(ob.values()))):
        for j in range(0, int(currencyList[i])):
            msg = msg + str(i) + "@"
            unblind = blindSign.payData(msg, int(list(ob.values())[i]["n"],16), int(list(ob.values())[i]["e"],16), int(list(ob.values())[i]["d"],16))
            data['sigma']=unblind
            data['msg']=msg
            print(data)
            tmp=data.copy()
            value.append(tmp)
    print(value)
    return value


def currencyVerify(request):
    payee = request.GET.get("payee")
    sigmaInput = request.GET.get("sigmaInput")
    msgInput = request.GET.get("msgInput")
    try:
        mod = SpendingInfo.objects  # 获取SpendingInfo模型的Model操作对象
        spending = mod.get(sigma=sigmaInput, msg=msgInput)
        spending.__dict__.pop("_state")
        print(spending.__dict__)
        return HttpResponse("双花")
    except:
        ob = Cryptocurrency.objects.order_by("-value")
        for i in range(0, len(list(ob.values()))):
            if blindSign.verify(int(sigmaInput,16),str(msgInput),int(list(ob.values())[i]["e"],16),int(list(ob.values())[i]["n"],16)):
                spendingOb=SpendingInfo()
                spendingOb.sigma=sigmaInput
                spendingOb.msg=msgInput
                spendingOb.save()
                userOb = User.objects
                thePayee = userOb.get(name=payee)
                thePayee.money=thePayee.money+int(list(ob.values())[i]["value"])
                thePayee.save()
                return HttpResponse('valid')
        return HttpResponse('invalid')

