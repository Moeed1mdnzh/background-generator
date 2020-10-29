import pygame
import random as r


pygame.init()

class board:
    ##########
    #OUR BOARD
    ##########
    def __init__(self,caption="generate",w=700,h=500,color=(0,0,0)):
        self.board = pygame.display.set_mode((w,h))
        self.caption = caption 
        pygame.display.set_caption(self.caption)
        self.color = color
        self.w,self.h = w,h
        self.font = pygame.font.SysFont("arial",50,"light")
        self.Text = self.font.render(self.caption,True,(200,200,200))
    def Board(self):
        self.board.fill(self.color)
    def box(self):
        pygame.draw.rect(self.board,(248, 252, 3),(self.h//2,self.w//2,220,110),10)
        pygame.draw.rect(self.board,(180,180,180),(10,10,680,320),15)
    def text(self):
        self.board.blit(self.Text,(260,370))

class shapes(board):
	def __init__(self):
		super().__init__()
		self.num =  r.randint(1,30)
		self.empty = r.randint(0,1)
	def bg(self,color):
		pygame.draw.rect(self.board,color,(10,10,672,320))
	def rect(self,color):
		self.num = r.randint(1,30)
		for i in range(self.num):
			self.empty = r.randint(0,1)
			w,h = r.randint(20,50),r.randint(20,50)
			x,y = r.randint(40,650),r.randint(40,270)
			pygame.draw.rect(self.board,color,(x,y,w,h),self.empty)
	def square(self,color):
		self.num = r.randint(1,30)
		for i in range(self.num):
			self.empty = r.randint(0,1)
			w=h=r.randint(20,50)
			x,y = r.randint(40,650),r.randint(40,270)
			pygame.draw.rect(self.board,color,(x,y,w,h),self.empty)
	def polygon(self,color):
		self.NUM = r.randint(1,15)
		for i in range(self.NUM):
			self.num = r.randint(1,30)
			points = []
			places = r.randint(3,9)
			for i in range(places):
				point = (r.randint(60,630),r.randint(60,250))
				points.append(point)
			for i in range(self.num):
				self.empty = r.randint(0,1)
				pygame.draw.polygon(self.board,color,points,self.empty)
	def circle(self,color):
		self.num = r.randint(1,30)
		radius = r.randint(5,20)
		for i in range(self.num):
			self.empty = r.randint(0,1)
			radius = r.randint(5,20)
			x,y = r.randint(40,650),r.randint(40,270)
			pygame.draw.circle(self.board,color,(x,y),radius,self.empty)
	def ellipse(self,color):
		self.num = r.randint(1,30)
		for i in range(self.num):
			self.empty = r.randint(0,1)
			x,y = r.randint(40,650),r.randint(40,270)
			w,h = r.randint(20,50),r.randint(20,50)
			pygame.draw.ellipse(self.board,color,(x,y,w,h),self.empty)

	