#
#This code could not be tested without Pi, which was not reading correct voltage
#


#import RPi.GPIO as GPIO
import GPIOSimulator as GPIO
from Morse_Translate import Morse

m = Morse()
m.__init__()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
start_light_time = 0
start_dark_time = 0
end_light_time = 0
end_dark_time = 0

while True:
    if GPIO.input(7) == 1:
        start_light_time = time.time()
        end_dark_time = time.time()
        if not start_dark_time == 0:
            if end_dark_time - start_dark_time > 7:
                done()
            m.get_space_input(end_dark_time - start_dark_time)
    elif GPIO.input(7) == 0:
        start_dark_time = time.time()
        end_light_time = time.time()
        if not start_light_time == 0:
            m.get_letter_input(end_light_time - start_light_time)

def done():
    GPIO.cleanup()
    temp = m.translate_input()
    result = m.output_result()
    print(result)
    exit()
