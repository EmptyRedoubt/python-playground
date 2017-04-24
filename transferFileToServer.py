import RPi.GPIO as GPIO
#from filetransfer import fileUpload #function called from filetransfer.py
import time
import os

#setup pin 18 BCM, pin 12 Board
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#variables of shell commands
fileTransfer = "/usr/bin/sshpass -p 'launch' scp -o StrictHostKeyChecking=no /home/pi/tempFile.txt ftpbob@52.40.103.214:/var/www/html/students"


        
#os.system('/usr/local/bin/gpio readall')
print("begin file transfer of file created during launchSetup script")
os.system(fileTransfer)     #transfer file to webserver
print('Transfer complete!')	
time.sleep(3)
