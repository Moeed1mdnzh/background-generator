import pygame
import random as r
import Frontend


class generate:
	def __init__(self,board,shapes):
		self.color = (r.randint(1,255),r.randint(1,255),r.randint(1,255))
		self.board = board
		self.shapes = shapes
		self.Func = r.choice([self.shapes.rect,self.shapes.polygon,
			self.shapes.circle,self.shapes.ellipse])
	def Generate(self):
		self.color = (r.randint(1,255),r.randint(1,255),r.randint(1,255))
		self.shapes.bg(self.color)
		self.color = (r.randint(1,255),r.randint(1,255),r.randint(1,255))
		self.Func(self.color)
		self.Func = r.choice([self.shapes.rect,self.shapes.polygon,
		self.shapes.circle,self.shapes.ellipse,self.shapes.square])
class main(generate):
	def quit_generate(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:
					self.pos = pygame.mouse.get_pos()
					if self.pos[0] in range(258,461) and self.pos[1] in range(357,452):
						self.Generate()
	def update(self):
		pygame.display.update()
	def delay(self):
		pygame.time.delay(100)
	def main(self):
		while True:
			self.delay()
			self.board.text()
			self.board.box()
			self.quit_generate()
			self.update()

if __name__ == "__main__":
	g = generate(Frontend.board(),Frontend.shapes())
	m = main(Frontend.board(),Frontend.shapes())
	m.main()