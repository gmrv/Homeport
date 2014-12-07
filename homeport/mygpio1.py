def setLed(state):
    print("Led turn on")

def getTemp():
    str1 = "7b 01 4b 46 7f ff 05 10 1d t=23687"
    equals_pos = str1.find('t=')
    if equals_pos != -1:
        temp_string = str1[equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
    return -999.0

def getButton():
    print("button not use")
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(3, GPIO.IN)
    # port3 = GPIO.input(3)
    # return -1
