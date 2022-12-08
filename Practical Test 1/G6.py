import RPi.GPIO as G
import time

try:
    G.setmode(G.BCM)
    G.setup(27,G.OUT)
    G.setup(22,G.OUT)
    G.setup(4,G.IN)
    
    t=0.5
    while True:
        while (G.input(4) == 0):
            print("You pressed button")
            G.output(27,True)
            G.output(22,True)
            time.sleep(t)
            G.output(27,False)
            G.output(22,False)
            
except KeyboardInterrupt:
    G.cleanup()
            
                     