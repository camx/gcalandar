#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import atexit

# OSPI PIN DEFINES
pin_relay =  15
status = 0

def main():
  print('OpenSprinkler Pi is running relay test...')

  GPIO.cleanup()
  # setup GPIO pins to interface with shift register
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin_relay, GPIO.OUT)

  while True:
    try:
        GPIO.output(pin_relay, True);
        time.sleep(1);
        GPIO.output(pin_relay, False);
        time.sleep(1);
    except:
      pass
 
def progexit():
  GPIO.cleanup()

if __name__ == "__main__":
  atexit.register(progexit)
  main()
