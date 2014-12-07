from django.http import HttpResponse
import mygpio
import os
import time


html1 = "<html><body><H1><a href='on'>on</a></br></br><a href='off'>off</a></H1></br>"
html2 = ""
html3 = "</body></html>"
port3 = 0


def home(request):
    html2 = "<b>" + mygpio.getTemp() + "</b>"


    return HttpResponse(html1+html2+html3)

def on(request):
    mygpio.setLedOn(1)
    html2 = "<b>" + mygpio.getTemp() + "</b>"
    return HttpResponse(html1+html2+html3)

def off(request):
    mygpio.setLedOn(0)
    html2 = "<b>" + mygpio.getTemp() + "</b>"
    return HttpResponse(html1+html2+html3)

