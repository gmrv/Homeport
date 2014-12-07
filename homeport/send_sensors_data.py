import socket
import mygpio

# MAC адрес устройства. Заменить на свой!
DEVICE_MAC = 'e8:4e:06:1c:37:e8'

# идентификатор устройства, для простоты добавляется 01 (02) к mac устройства
SENSOR_ID_1 = '28-000005ffad2a'
#SENSOR_ID_2 = DEVICE_MAC + '02'

# значения датчиков, тип float/integer
sensor_value_1 = mygpio.getTemp()
#sensor_value_2 = -20.25

# создание сокета
sock = socket.socket()

# обработчик исключений
try:
    # подключаемся к сокету
    sock.connect(('narodmon.ru', 8283))

    # пишем в сокет еденичное значение датчика
    sock.send("#{}\n#{}#{}\n##".format(DEVICE_MAC, SENSOR_ID_1, sensor_value_1))

    # пишем в сокет множественные значение датчиков
    # sock.send("#{}\n#{}#{}\n#{}#{}\n##".format(DEVICE_MAC, SENSOR_ID_1, sensor_value_1, SENSOR_ID_2, sensor_value_2))

    # читаем ответ
    data = sock.recv(1024)
    sock.close()
    print data
except socket.error, e:
    print('ERROR! Exception {}'.format(e))
