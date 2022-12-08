import RPi.GPIO as G
import time

try:
    G.setmode(G.BCM)
    G.setup(27,G.OUT)
    
    t=1.5
    while True:
        G.output(27,True)
        time.sleep(t)
        G.output(27,False)
        time.sleep(t)
except KeyboardInterrupt:
    G.cleanup()