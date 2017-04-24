import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)

output = True

while 1:
    GPIO.output(22, output)
    output = not output
    sleep(.000005)
    print(output)

GPIO.cleanup()
