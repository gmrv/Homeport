from django.http import HttpResponse
import mygpio
import os
from datetime import datetime

#iplog_fpath = ""
iplog_fpath = "/home/pi/homeport/"
html1 = "<html><body><H1><a href='on'>on</a></br></br><a href='off'>off</a></H1></br>"
html2 = ""
html3 = "</body></html>"
port3 = 0


def home(request):
    html2 = "<b>" + str(mygpio.getTemp()) + "</b>"

    f = open(iplog_fpath + "ip.log", 'a')
    f.write(str(datetime.now()) + " " + request.META['REMOTE_ADDR'] + "; " + request.META['COMPUTERNAME']  + "; " + request.META['USERNAME']   + "; " + request.META['TMP'] + "; " + "\\off" + "\r\n")
    f.close()

    return HttpResponse(html1+html2+html3)

def on(request):
    mygpio.setLed(1)
    html2 = "<b>" + str(mygpio.getTemp()) + "</b>"

    f = open(iplog_fpath + "ip.log", 'a')
    f.write(str(datetime.now()) + " " + request.META['REMOTE_ADDR'] + "; " + request.META['COMPUTERNAME']  + "; " + request.META['USERNAME']   + "; " + request.META['TMP'] + "; " + "\\off" + "\r\n")
    f.close()

    return HttpResponse(html1+html2+html3)

def off(request):
    mygpio.setLed(0)
    html2 = "<b>" + str(mygpio.getTemp()) + "</b>"

    f = open(iplog_fpath + "ip.log", 'a')
    f.write(str(datetime.now()) + " " + request.META['REMOTE_ADDR'] + "; " + request.META['COMPUTERNAME']  + "; " + request.META['USERNAME']   + "; " + request.META['TMP'] + "; " + "\\off" + "\r\n")
    f.close()

    return HttpResponse(html1+html2+html3)

def log(request):
    html2 = ""
    line = ""
    f = open(iplog_fpath + "ip.log", 'r')

    for line in f:
        html2 += line + "</br>"

    f.close()

    return HttpResponse(html1+html2+html3)