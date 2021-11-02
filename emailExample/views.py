from django.shortcuts import render
from .tasks import test_func, send_mail_func
from django.http import HttpResponse


# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("<h2>Mail Send Successfully</h2>")

