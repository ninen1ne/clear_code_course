# 20/7/2024
import pygame, sys
from random import randint, uniform

class Ship(pygame.sprite.Sprite):
	""" """
	def __init__(self, groups):
		# 1) we have to init the parent class
		super().__init__(groups) 

		# 2) we need a surface -> image
		self.image = pygame.image.load('graphics/mushroom2.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (100, 100))

		# 3) we need a rect
		self.rect = self.image.get_frect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

		# 4) add a mask
		self.mask = pygame.mask.from_surface(self.image)

		# laser time 
		self.can_shoot = True
		self.shoot_time = None
		
		# import sound 
		self.laser_sound = pygame.mixer.Sound('sounds/laser.ogg')
		self.laser_sound.set_volume(0.3)

	def input_position(self):
		pos = pygame.mouse.get_pos()
		self.rect.center = pos

	def laser_timer(self, duration=500):
		# determine speed of creating new laser obj
		if not self.can_shoot:
			current_time = pygame.time.get_ticks()
			if current_time - self.shoot_time > duration:
				self.can_shoot = True


	def laser_shoot(self):
		if pygame.key.get_just_pressed()[pygame.K_SPACE] and self.can_shoot == True:
			self.can_shoot = False
			self.shoot_time = pygame.time.get_ticks()
			Laser(self.rect.midtop, laser_group)
			self.laser_sound.play() 

	def meteor_collision(self):
		if pygame.sprite.spritecollide(self,meteor_group , False, pygame.sprite.collide_mask):
			pygame.quit()
			sys.exit()


	def update(self):
		self.laser_timer()
		self.laser_shoot()
		self.input_position()
		self.meteor_collision()


class Laser(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)
		self.image = pygame.image.load('graphics/laser.png').convert_alpha()
		self.rect = self.image.get_frect(midbottom = pos)
		self.mask = pygame.mask.from_surface(self.image)

		# float based position
		self.pos = pygame.math.Vector2(self.rect.topleft)
		self.direction = pygame.math.Vector2(0, -1)
		self.speed = 300

		# import sound 
		self.explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')
		self.explosion_sound.set_volume(0.6)

	def meteor_collision(self):
		if pygame.sprite.spritecollide(self, meteor_group, True, pygame.sprite.collide_mask):
			self.kill()
			self.explosion_sound.play()


	def update(self):
		self.pos += self.direction * self.speed * dt 
		self.rect.topleft = (self.pos.x, self.pos.y)

		if self.rect.bottom < 0:
			self.kill()
		self.meteor_collision()


class Meteor(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)
		# basic setup
		meteor_surf = pygame.image.load('graphics/meteor.png').convert_alpha()
		# randomizing the meteor size
		meteor_size = pygame.math.Vector2(meteor_surf.get_size()) * uniform(0.75, 2)
		self.scaled_surf = pygame.transform.scale(meteor_surf, meteor_size)
		self.image = self.scaled_surf
		self.rect = self.image.get_frect(center = pos)
		self.mask = pygame.mask.from_surface(self.image)

		# float based positioning
		self.pos = pygame.math.Vector2(self.rect.topleft)
		self.direction = pygame.math.Vector2(uniform(-0.5, 0.5),1)
		self.speed = randint(400, 600)

		# rotation logic 
		self.rotation = 0
		self.rotation_speed = (randint(20, 50))

	def rotate(self):
		self.rotation += self.rotation_speed * dt
		rotated_surf = pygame.transform.rotozoom(self.scaled_surf, self.rotation, 1)
		self.image = rotated_surf
		self.rect = self.image.get_frect(center = self.rect.center)
		self.mask = pygame.mask.from_surface(self.image)

	def update(self):
		self.pos += self.direction * self.speed * dt
		self.rect.topleft = (self.pos.x, self.pos.y)
		self.rotate()

		if self.rect.top > SCREEN_HEIGHT:
			self.kill()


class Score:
	def __init__(self):
		self.font = pygame.font.Font('graphics/subatomic.ttf', 50)
		
	def display(self):
		score_text = f'score {pygame.time.get_ticks() // 100}'
		text_surf = self.font.render(score_text, True, (255, 255, 255))
		text_rect = text_surf.get_frect(midbottom =(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 80))
		display_surf.blit(text_surf, text_rect)
		pygame.draw.rect(display_surf,
				    (255, 255, 255),
					text_rect.inflate(30, 30),
					width=8,
					border_radius= 5)

# basic setup 
pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
display_surf = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Asteroid Shooter')

# background
background_surf = pygame.image.load('graphics/background.png').convert()

# sprite groups
spaceship_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()

# sprite creation
ship = Ship(spaceship_group)

# meteor timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

# score
score = Score()

# sound 
background_music = pygame.mixer.Sound('sounds/music.wav')
background_music.play(loops = -1)
background_music.set_volume(0.3)

running = True 
while running:
	# delta time
	dt = clock.tick(120) / 1000

	
	# event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == meteor_timer:
			meteor_y_pos = randint(-100, -50)
			meteor_x_pos = randint(-100, SCREEN_WIDTH + 100)
			Meteor(pos=(meteor_x_pos, meteor_y_pos), groups=meteor_group)

	# background
	display_surf.blit(background_surf, (0, 0)) # this must be the first thing U blit

	# update
	spaceship_group.update()
	laser_group.update()
	meteor_group.update()
	score.display()

	# graphics
	spaceship_group.draw(display_surf)
	laser_group.draw(display_surf)
	meteor_group.draw(display_surf)

	# draw the game
	pygame.display.update()

pygame.quit()
