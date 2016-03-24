
import time
import sys
import serial
import os
from traitement_protocole import*

os.system("echo BB-UART1 > /sys/devices/bone_capemgr.8/slots")
time.sleep(2)
uart = serial.Serial(port="/dev/ttyO1" , baudrate=115200)

protocole = Traitement_protocole()

while 1:
	data = uart.readline()
	protocole.traitement_trame(data)
