import pygame
import math
import constants


class Weapon():
    def __init__(self, image, arrow_image) -> None:
        self.original_image = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.arrow_image = arrow_image
        self.rect = self.image.get_rect()
        self.fired = False
        self.last_shot = pygame.time.get_ticks()

    def update(self, player):
        shot_cooldown = 300

        arrow = None
        self.rect.center = player.rect.center

        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect.centerx
        # negative because pygame y coords increase down the screen
        y_dist = -(pos[1] - self.rect.centery)
        self.angle = math.degrees(math.atan2(y_dist, x_dist))

        # get mouseclick
        if pygame.mouse.get_pressed()[0] and not self.fired and (pygame.time.get_ticks() - self.last_shot) >= shot_cooldown:
            arrow = Arrow(self.arrow_image, self.rect.centerx,
                          self.rect.centery, self.angle)
            self.fired = True
            self.last_shot = pygame.time.get_ticks()

        # reset mouse click
        if not pygame.mouse.get_pressed()[0]:
            self.fired = False

        return arrow

    def draw(self, surface):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width()/2)),
                     self.rect.centery - int(self.image.get_height()/2)))


class Arrow(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        self.angle = angle
        self.image = pygame.transform.rotate(
            self.original_image, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # calculate the horizontal and vertical speed based on the angle
        self.dx = math.cos(math.radians(self.angle)) * constants.ARROW_SPEED
        # negative because pygame y coords increases down the screen
        self.dy = -(math.sin(math.radians(self.angle)) * constants.ARROW_SPEED)

    def update(self):
        # reposition based on speed
        self.rect.x += self.dx
        self.rect.y += self.dy

        # check if arrow has gone off screen
        if self.rect.right < 0 or self.rect.left > constants.SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > constants.SCREEN_HEIGHT:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width()/2)),
                     self.rect.centery - int(self.image.get_height()/2)))
