import pygame
import constants
from character import Character

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Crawler")

#create clock for maintaining frame rate
clock = pygame.time.Clock()

#define player movement variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

#helper function to scale image
def scale_img(image, scale):
  w = image.get_width()
  h = image.get_height()
  return pygame.transform.scale(image, (w * scale, h * scale))

animation_types = ['idle', 'run']
#load images
animations_list = []

for animation in animation_types:
  #reset temporary list of images
  temp_list = []
  for i in range(4):
    img = pygame.image.load(f'assets/images/characters/elf/{animation}/{i}.png').convert_alpha()
    img = scale_img(img, constants.SCALE)
    temp_list.append(img)

  animations_list.append(temp_list)

#create player
player = Character(100, 100, animations_list)

#main game loop
run = True
while run:

  #control frame rate
  clock.tick(constants.FPS)

  screen.fill(constants.BG)

  #calculate player movement
  dx = 0
  dy = 0
  if moving_right == True:
    dx = constants.SPEED
  if moving_left == True:
    dx = -constants.SPEED
  if moving_up == True:
    dy = -constants.SPEED
  if moving_down == True:
    dy = constants.SPEED

  #move player
  player.move(dx, dy)

  #update player
  player.update()

  #draw player on screen
  player.draw(screen)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    #take keyboard presses
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        moving_left = True
      if event.key == pygame.K_d:
        moving_right = True
      if event.key == pygame.K_w:
        moving_up = True
      if event.key == pygame.K_s:
        moving_down = True

    #keyboard button released
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_a:
        moving_left = False
      if event.key == pygame.K_d:
        moving_right = False
      if event.key == pygame.K_w:
        moving_up = False
      if event.key == pygame.K_s:
        moving_down = False

  pygame.display.update()

pygame.quit()