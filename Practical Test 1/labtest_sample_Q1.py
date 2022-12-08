#Lab Test Sample, solution

import RPi.GPIO as G
import time

count = 0

def on_LED(on_seconds, off_seconds):    
    G.output(27, True)
    time.sleep(on_seconds)
    G.output(27, False)
    time.sleep(off_seconds)
         
         
    

try:
    G.setmode(G.BCM)
    G.setup(27, G.OUT)
    G.setup(4, G.IN)
    G.setup(5, G.IN)
    
    while True:
        while(G.input(4) == 0):
            count += 1
            print(f'U pressed {count}') #w/o delay, this msg will be printed many times
            on_LED(1, 0)             
             
        while(G.input(5) == 0):
            if count > 0:
                count -= 1
                            
                print(f'Button_2 pressed {count}') #w/o delay, this msg will be printed many times
                on_LED(0.5, 0.5)
                on_LED(0.5, 0.5)
                
            else:
                print(f'Button_2 pressed {count}')
                on_LED(0.5, 0.5)
                on_LED(0.5, 0.5)
                on_LED(0.5, 0.5)
            
            
except KeyboardInterrupt:
    G.cleanup()