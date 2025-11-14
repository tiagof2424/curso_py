import pygame as pg
# create template enemies
class Enemies (pg.sprite.Sprite): #hereda las imagenes de pygame(herencia)
  def __init__(self,position,image):
    pg.sprite.Sprite.__init__(self)
    self.image= image
    self.rect = self.image.get_rect()
    self.rect.center = position

  def update(self):
    self.move()

  #mover al enemigo
  def move(self):
    self.rect.x +=1