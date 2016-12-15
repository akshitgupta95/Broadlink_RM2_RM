#!/usr/bin/python

from working.working import rm
import time
import sys
import binascii
import base64

device = rm(host=("192.168.1.60",80), mac=bytearray.fromhex("B4430daa8142"))

print "Connecting to Broadlink device...."
device.auth()
time.sleep(1)
print "Connected...."

codeName = raw_input("Please Enter Code Name  e.g. tvOff ")
time.sleep(1)
print "When Broadlink white led is lit press the button on your remote within 5 seconds"

device.host
device.enter_learning()
time.sleep(5)
ir_packet = device.check_data()
#convert code to hex
myhex = base64.b64encode(ir_packet).decode('utf8'); 

if ir_packet == None:
   print "No button press read - quitting"
   sys.exit()
else:

# record learned hex code to file
   f = open(codeName +".txt",'w')
f.write(myhex)
f.close()

print "Hex code written to file named " + codeName + ".txt"