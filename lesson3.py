import private 
import requests

# url = f'https://maker.ifttt.com/trigger/button_press/with/key/{private.iftttKey}?value1=31c&value2=51'

# r = requests.get(url)
# if r.status_code == 200:
#     print("發送成功")

from gpiozero import Button
from gpiozero import RGBLED
from signal import pause

# def say_hello():
#     print("Hello!")

# button = Button(18)

# button.when_pressed = say_hello

state = False
counter = 0
url = f'https://maker.ifttt.com/trigger/button_press/with/key/{private.iftttkey}?value1=31c&value2=51'
private.iftttkey
def user_press():
    global state,counter
    state = not state
    if state == True:
        print("開燈")
        counter+=1
        if counter %3 == 1:
            led.color=(0,1,0)
        elif counter %3 ==2:
            led.color=(0,0,1)
        elif counter %3==0:
            led.color=(1,0,0)
    
        r = requests.get(url)
        if r.status_code == 200:
                print("發送成功")

    else:
        print("關燈")
        led.color=(0,0,0)

button = Button(18)
led = RGBLED(red=17, green=27, blue=22)

button.when_pressed = user_press

pause()