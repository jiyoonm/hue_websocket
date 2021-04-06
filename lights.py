from phue import Bridge
from ip_address import bridge_ip_address
from pulse import *
from threading import Thread


import time

def access_lights(bridge_ip_address):
    b = Bridge(bridge_ip_address)
    light_names_list = b.get_light_objects('id')
    return light_names_list

def client1_pulse(pulse):

    lights = access_lights(bridge_ip_address)
    print(pulse)
    time.sleep(pulse)
    lights[1].on = True
    lights[1].hue = 180
    lights[1].saturation = 100
    lights[1].brightness=250

    time.sleep(pulse)
    lights[1].brightness=127

def client2_pulse(pulseB):
    lights = access_lights(bridge_ip_address)
    time.sleep(pulseB)
    lights[2].on = True
    lights[2].hue = 180
    lights[2].saturation = 100
    lights[2].brightness=250

    time.sleep(pulseB)
    lights[2].brightness=127

