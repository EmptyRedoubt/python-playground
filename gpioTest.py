import RPi.GPIO as GPIO
##from time import sleep
##
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
###GPIO.output(22, False)
##
##output = True
##
##for blink in range(20):
##    GPIO.output(22, output)
##    output = not output
##    sleep(.1)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(1):
    switchState=GPIO.input(7)
    GPIO.output(22, switchState)
    print(switchState)

GPIO.cleanup()
