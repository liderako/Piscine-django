from django.conf import settings

class Player:
	def __init__(self, position):
		self.x = position[0]
		self.y = position[1]
		self.max_x = settings.DEFAULT_GAME_SIZE
		self.max_y = settings.DEFAULT_GAME_SIZE
		self.min_x = 0
		self.min_y = 0

	def 	moveUp(self):
		if (self.y > self.min_x):
			self.y -= 1

	def 	moveDown(self):
		if (self.y < self.max_x):
			self.y += 1

	def 	moveRight(self):
		if (self.x < self.max_x):
			self.x += 1

	def 	moveLeft(self):
		if (self.x > self.min_x):
			self.x -= 1

	def 	getPosition(self):
		return ([self.x, self.y])
