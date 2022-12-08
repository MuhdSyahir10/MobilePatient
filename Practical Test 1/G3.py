import RPi.GPIO as G
import time
G.setwarnings(False)


G.setmode(G.BCM)
G.setup(27,G.OUT)
G.setup(22,G.OUT)

G.output(27,True)
G.output(22,True)

time.sleep(3)

G.output(27,False)
G.output(22,False)

time.sleep(3)

input("Hit<Enter> key to exit this prog")
G.setwarnings(False)

G.cleanup()
