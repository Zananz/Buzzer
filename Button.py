import time
from gpiozero import Button
import simpleaudio as sa

#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(2,GPIO.IN)

Button= Button(2)


wave_obj = sa.WaveObject.from_wave_file("/home/pi/Dokumente/Python/Button.wav")


while 1:
    if  Button.is_pressed:
        
        play= wave_obj.play()
        play.wait_done()
        time.sleep(0.7)
        
    else:
        pass
         
         