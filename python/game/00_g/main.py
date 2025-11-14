import pygame as pg
import os 
from enemies import Enemies

#configuracion de la ventana 
screen_width = 800
screen_height = 800
fps = 60

#iniciar pygame
pg.init()
screen = pg.display.set_mode((screen_width,screen_height))
#crear un clock
clock = pg.time.Clock()
#cargar imagenes

enemy_image = pg.image.load (os.path.join("python/game/00_g/asset/enemies",""))
#agregar al grupo enemigo
enemies_group =pg.sprite.Group()
#crear enemigos
enemi_one = Enemies((300,300),enemy_image)
enemies_group.add(enemi_one)
#gameloop 
run = True
while run:
    #escuchar el evento quit
    for event in pg.event.get ():
        #seleccionar el evento quit
        if event.type == pg.QUIT:
            run =False
    screen.fill("gray100")

    #llamar al metodo update del enemigo
    enemies_group.update()
    #dibujar al enemigo en la pantalla
    enemies_group.draw(screen)
    clock.tick(fps)
    #actualiozar la ventana 
    pg.display.flip()
pg.quit()