from django.http import HttpResponse
import mygpio1
import os
from datetime import datetime


html1 = "<html><body><H1><a href='on'>on</a></br></br><a href='off'>off</a></H1></br>"
html2 = ""
html3 = "</body></html>"
port3 = 0


def home(request):
    html2 = "<b>" + str(mygpio1.getTemp()) + "</b>"

    f = open("/home/pi/homeport/ip.log", 'a')
    f.write(str(datetime.now()) + " " + str(request.META['REMOTE_ADDR']) + "\\" + "\r\n")
    f.close()

    return HttpResponse(html1+html2+html3)

def on(request):
    mygpio1.setLed(1)
    html2 = "<b>" + str(mygpio1.getTemp()) + "</b>"

    f = open("/home/pi/homeport/ip.log", 'a')
    f.write(str(datetime.now()) + " " + str(request.META['REMOTE_ADDR']) + "\\on" + "\r\n")
    f.close()

    return HttpResponse(html1+html2+html3)

def off(request):
    mygpio1.setLed(0)
    html2 = "<b>" + str(mygpio1.getTemp()) + "</b>"

    f = open("/home/pi/homeport/ip.log", 'a')
    f.write(str(datetime.now()) + " " + str(request.META['REMOTE_ADDR']) + "\\off" + "\r\n")
    f.close()

    return HttpResponse(html1+html2+html3)

def log(request):
    html2 = ""
    line = ""
    f = open("/home/pi/homeport/ip.log", 'r')

    for line in f:
        html2 += line + "</br>"

    f.close()

    return HttpResponse(html1+html2+html3)