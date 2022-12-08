import RPi.GPIO as G

G.setmode(G.BCM)
G.setup(27,G.OUT)
G.output(27,True)
input("Press <Enter> key to turn ON LED & exit this prog")
G.output(27,False)
G.cleanup()
