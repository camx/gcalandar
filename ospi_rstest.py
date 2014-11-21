#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import atexit

# OSPI PIN DEFINES
pin_rs = 14

def main():
  print('OpenSprinkler Pi is running relay test...')

  GPIO.cleanup()
  # setup GPIO pins to interface with shift register
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin_rs, GPIO.IN)

  while True:
    try:
        if GPIO.input(pin_rs):
            print("Input is HIGH")
        else:
            print("Input is LOW")
        time.sleep(1);
    except:
      pass
 
def progexit():
  GPIO.cleanup()

if __name__ == "__main__":
  atexit.register(progexit)
  main()
