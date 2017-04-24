import RPi.GPIO as GPIO
import datetime
import time

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)
 
        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low
 
        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
 
        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1
 
        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout
        
# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25
LIGHTS = 17

# set up the SPI interface pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
GPIO.setup(LIGHTS, GPIO.OUT)
# loop on reading ADC value and 
#  printing the value
count = 0
while(count < 12):
        i = open('/var/www/tempWriteFile.csv', 'a')
        adcValue = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
        voltage = adcValue * (3300 / 1024)
        tempC = (voltage - 500) / 10
        tempF = tempC * 9 / 5 + 32
        current = datetime.datetime.now()
        i.write(str(tempF))
        i.write(',')
        i.write('%s/%s/%s' % (current.day, current.month, current.year))
        i.write(',')
        i.write('%s:%s:%s' % (current.hour, current.minute, current.second))
        i.write('\n')
        count += 1
        if tempF <= 65:
            GPIO.output(LIGHTS, True)
        elif tempF > 65:
            GPIO.output(LIGHTS, False)
        i.close()
        time.sleep(5)                     
