import RPi.GPIO as G
import time
G.setwarnings(False)

try:
    G.setmode(G.BCM)
    G.setup(27,G.OUT)
    G.setup(22,G.OUT)
    G.setup(4,G.IN)
    
    count=0
    t=0.5
    while True:
        if (G.input(4) == 0):
            count+=1
            print("You pressed button "+ str(count) + "number of times")
            G.output(27,True)
            G.output(22,True)
        else:
            time.sleep(t)
            G.output(27,False)
            G.output(22,False)
            
except KeyboardInterrupt:
    G.cleanup()
            
                     