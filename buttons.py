import pygame

#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, screen):
		screen.blit(self.image, (self.rect.x, self.rect.y))
  
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom):
			return True
		return False