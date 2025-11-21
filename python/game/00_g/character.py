import pygame as pg

#crear una plantilla de jugador
class Character (pg.sprite.Sprite):
  def __init__(self,poss,image) -> None:
    pg.sprite.Sprite.__init__(self)
    self.image=image
    self.rect=self.image.get_rect()
    self.rect.center=poss

  def move_x(self,new_pos):#metodo
    self.rect.x += new_pos
  
  def move_left(self,new_pos):
    self.rect.x -=new_pos

  def move_up(self,new_pos):
    self.rect.y -= new_pos

  def move_down(self,new_pos):
    self.rect.y += new_pos



