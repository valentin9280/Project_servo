import serial
import os
import time
import sys
sys.path.append("../Traitement")
from traitement_protocole import*

os.system("echo BB-UART1 > /sys/devices/bone_capmgr.8/slots")

uarts = serial.Serial(port="/dev/tty01" , baudrate=115200 , time =None)

protocole = Traitement_protocole()

while 1:
	data = uart.readline()
	protocole.traitement_trame(data)