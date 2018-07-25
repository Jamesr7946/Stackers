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
		pygame.time.set_timer(USEREVENT +1, 170)
		x=0
		y =0
		z=0
		while self.gaming:
		
			for event in pygame.event.get():
				if event.type == KEYDOWN: 
					sense.set_pixel(x, y, (255, 20, 255))
					if y==0:
						counter = x
					if y< 8:
						if x==counter:	
							y = y+1 	
							if y==8:
								pink = (255, 20, 147)
								blue = (0, 255, 255)
								speed = 0.2
								message = 'U won'
								sense.show_message(message, speed, blue, pink)
								time.sleep(1)	
								exit()	
											
						else: 
							pink = (255, 20, 147)
							blue = (0, 255, 255)
							speed = 0.2
							message = 'Loser'
							sense.show_message(message, speed, blue, pink)
							time.sleep(1)	
							exit()	
				else:				
					a = random.randint(0,255)
					b = random.randint(0,255)
					c = random.randint(0,255)
					color = (a, b, c)
					sense.set_pixel (x, y, color)
					time.sleep(0.13)
					sense.set_pixel(x, y, (0, 0, 0))
					z=x
					x = x+1
					
					if x==8:
						x=0
					
				
				
					
if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear() 
