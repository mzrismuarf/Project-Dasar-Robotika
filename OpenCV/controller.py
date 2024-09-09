import pyfirmata

comport = 'COM11'

board = pyfirmata.Arduino(comport)


led_1 = board.get_pin('d:7:o')
led_2 = board.get_pin('d:8:o')
led_3 = board.get_pin('d:9:o')
led_4 = board.get_pin('d:10:o')
led_5 = board.get_pin('d:11:o')


def led(fingerUp):
    led_1.write(fingerUp[0])
    led_2.write(fingerUp[1])
    led_3.write(fingerUp[2])
    led_4.write(fingerUp[3])
    led_5.write(fingerUp[4])
