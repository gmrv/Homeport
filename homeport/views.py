from django.http import HttpResponse
import os
import RPi.GPIO as GPIO
import time


html1 = "<html><body><H1><a href='on'>on</a></br></br><a href='off'>off</a></H1></br>"
html2 = ""
html3 = "</body></html>"
port3 = 0


def home(request):
    f = open("/sys/bus/w1/devices/28-000005ffad2a/w1_slave", 'r')
    f.readline()
    str1 = f.readline()
    html2 = "<b>" + str1 + "</b>"

    #GPIO.setup(3, GPIO.IN)
    #port3 = GPIO.input(3)
    #html2 = "<b>port3 (0-closed, 1-opened) = " + str(port3) + "</b>"
    return HttpResponse(html1+html2+html3)

def on(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    GPIO.output(3, 1)

    f = open("/sys/bus/w1/devices/28-000005ffad2a/w1_slave", 'r')
    str1 = f.readline()
    str1 = f.readline()
    html2 = "<b>" + str1 + "</b>"
    return HttpResponse(html1+html2+html3)

def off(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    GPIO.output(3, 0)

    f = open("/sys/bus/w1/devices/28-000005ffad2a/w1_slave", 'r')
    str1 = f.readline()
    str1 = f.readline()
    html2 = "<b>" + str1 + "</b>"

    #GPIO.cleanup()
    return HttpResponse(html1+html2+html3)

