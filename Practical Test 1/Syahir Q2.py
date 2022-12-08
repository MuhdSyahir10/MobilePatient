import RPi.GPIO as G
import time
G.setwarnings(False)


def LED(LED,on,off):
    if LED == "red":
        G.output(27,1)
        time.sleep(on)
        G.output(27,0)
        time.sleep(off)
    else:
        G.output(22,1)
        time.sleep(on)
        G.output(22,0)
        time.sleep(off)
        
c = 0
no_big = 0
no_small = 0
    
try:
    G.setwarnings(False)  #supress warning messages
    
    G.setmode(G.BCM)
    G.setup(27, G.OUT)
    G.setup(22, G.OUT)
    G.setup(4, G.IN)
    
    while True:
        diam = float(input("Enter diameter of dust particle:"))
        if (diam>50):
            no_big +=1
            print(f"Number of big particles: {no_big} ")
            LED('red',1,0)
            for i in range(150): #3s to undo the wrong diam he just entered
                if G.input(4) == 0:
                    no_big -=1
                    print("button pressed")
                    print(f"Number of big particles: {no_big} ")
                    break
                else:
                    time.sleep(0.02)
                    
        else:
            no_small +=1
            print(f"Number of small particles: {no_small} ")
            LED('green',1,0)
            for i in range(150): #3s to undo the wrong diam he just entered
                if G.input(4) == 0:
                    no_small -=1
                    print("button pressed")
                    print(f"Number of big particles: {no_small} ")
                    break
                else:
                    time.sleep(0.02)
            
        
except KeyboardInterrupt:
    G.cleanup()
    
    