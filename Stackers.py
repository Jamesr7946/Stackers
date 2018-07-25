from sense_hat import SenseHat
from pygame.locals import *
import pygame
import random
import time
#shows the class structure for gaming mode
sense = SenseHat()
sense.clear()
counter =0 



class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640, 480))
		self.gaming = True
	def startGame(self):
		pygame.time.set_timer(USEREVENT +1, 800)
		while self.gaming:
			for event in pygame.event.get():
				x=0
				while counter ==0:  #if u press a key it does this
					
					y = 0
					a = random.randint(1,255)
					b = random.randint(1,255)
					c = random.randint(1,255)
					color = (a, b, c)
					sense.set_pixel (x, y, color)
					time.sleep(1)
					sense.set_pixel(x, y, (0, 0, 0))
					x = x+1
					if x==8:
						x=0
					
if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear() 
