from django.shortcuts import render
from django.http import HttpResponse
import web.RSA_03test as blindSign


# Create your views here.
def index(request):
    return render(request, "../templates/test.html")


def test(request):
    name = request.GET.get("name")
    return HttpResponse("Hello " + name)


def blind(request):
    a=blindSign.blind()
    return HttpResponse(str(hex(a)))
