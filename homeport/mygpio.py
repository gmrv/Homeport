import RPi.GPIO as GPIO

def setLedOn(state):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    GPIO.output(3, state)

def getTemp():
    f = open("/sys/bus/w1/devices/28-000005ffad2a/w1_slave", 'r')
    f.readline()
    str1 = f.readline()
    return str1

def getButton():
    print("Отключено")
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(3, GPIO.IN)
    # port3 = GPIO.input(3)
    # return -1
