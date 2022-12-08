import RPi.GPIO as G
import time
G.setwarnings(False)

c = 0

def LED(on,off):
    G.output(27,1)
    time.sleep(on)
    G.output(27,0)
    time.sleep(off)
    
try:
    G.setmode(G.BCM)
    G.setup(27, G.OUT)
    G.setup(4, G.IN)
    G.setup(5, G.IN)

    while True:
        while (G.input(4) == 0):
            c +=1
            print(f"You pressed button {c} time")
            LED(1,0)
            
        while (G.input(5) == 0):
            c -=1
            #print(f"You pressed button {c} time")
            LED(0.5,0.5)
            if c < 0:
                LED(0.5,0.5)
                LED(0.5,0.5)
                LED(0.5,0.5)
                break
            print(f"You pressed button {c} time")
            
            
except KeyboardInterrupt:
    G.cleanup()