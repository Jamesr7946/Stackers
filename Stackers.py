from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
#shows the class structure for gaming mode
sense = SenseHat()
sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640, 480))
		self.gaming = True
	def startGame(self):
		pygame.time.set_timer(USEREVENT +1, 800)
		while self.gaming:
			for event in pygame.event.get():
				if event.type == KEYDOWN: #if u press a key it does this
					sense.set_pixel (1, 5, (130, 45, 255))		
				else:
					sense.set_pixel (1, 6, (0, 140, 85))
					
if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear() 
