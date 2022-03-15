from operator import truediv
import RPi.GPIO as GPIO

pwmLED1 = 26 # Pulse width modulation
led2 = 13
btnPin = 2

GPIO.setwarnings(False)

# Pin setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering
GPIO.setup(led2, GPIO.OUT)
pwm = GPIO.PWM(pwmLED1, 1) # Initialise la led a X hertz par seconde
GPIO.setup(pwmLED1, GPIO.OUT)

# Setup Initial
GPIO.output(led2, GPIO.LOW)
try:
    while True:
        GPIO.output(led2, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(led2, GPIO.HIGH)
        time.sleep(0.1)

except KeyboardInterrupt: # Si CTRL-C exit
    GPIO.cleanup() # Réinitialise les pins