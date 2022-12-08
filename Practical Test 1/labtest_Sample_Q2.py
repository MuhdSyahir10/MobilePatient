#Lab Test Sample, Question 2,  solution

import RPi.GPIO as G
import time

no_of_small = 0
no_of_big = 0

def on_LED(LED, on_seconds, off_seconds):
    if LED == 'red':
        G.output(27, True)
        time.sleep(on_seconds)
        G.output(27, False)
        time.sleep(off_seconds)
    else:  #assume Green LED if it's not Red
        G.output(22, True)
        time.sleep(on_seconds)
        G.output(22, False)
        time.sleep(off_seconds)        
         
         
    

try:
    G.setwarnings(False)  #supress warning messages
    
    G.setmode(G.BCM)
    G.setup(27, G.OUT)
    G.setup(22, G.OUT)
    G.setup(4, G.IN)
    G.setup(5, G.IN)
    
    print('This prog count the no. of large & small dust particles...')
    
    while True:
        diam = float( input('Enter dust partical diameter (in mico-meter): ') )
        if (diam > 50):
            no_of_big += 1
            print(f"no. of big dust particles = {no_of_big}")            
            on_LED('red', 1, 0)
            
            print('Press button to undo wrongly entered big diameter...')
            for i in range(150):  #give use 3s to undo the wrong diam he just entered                                
                if G.input(4) == 0:                    
                    no_of_big -=1
                    print('Button pressed. ')
                    print(f"no. of big dust particles is: {no_of_big}")
                    break  #button already pressed. No need to detech button-press anymore
                else:
                    time.sleep(0.02)  #0.02s x 150 = 3s 
                    
            
        else:
            no_of_small += 1
            print(f"no. of Small dust particles = {no_of_small}")
            on_LED('green', 1, 0)

            print('Press button to undo wrongly entered Small diameter...')
            for i in range(150):  #give use 3s to undo the wrong diam he just entered                                
                if G.input(4) == 0:                    
                    no_of_small -=1
                    print('Button pressed. ')
                    print(f"no. of Small dust particles is: {no_of_small}")
                    break  #button already pressed. No need to detech button-press anymore
                else:
                    time.sleep(0.02)  #0.02s x 150 = 3s 
            
            
            
except KeyboardInterrupt:
    G.cleanup()
