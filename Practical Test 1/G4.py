import RPi.GPIO as G
import time
G.setwarnings(False)

G.setmode(G.BCM)
G.setup(27,G.OUT)

def Blink(numTimes, length):
    for i in range(0, numTimes):
        print("iteration" + str(i+1))
        
        G.output(27,1)
        time.sleep(length)
        
        G.output(27,0)
        time.sleep(length)
        
    print("Done")
    G.cleanup()
        
iterations=input("Enter total number of times to blink:")
duration=input("Enter duration of each ON/OFF state(seconds):")

Blink(int(iterations),float(duration))