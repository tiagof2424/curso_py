import pygame as pg
import os 
from enemies import Enemies
from character import Character
cwd =os.getcwd()
print()

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

enemy_image =pg.image.load (os.path.join(cwd,"pr/games/01_g/asset/enemies/enemy1.png"))
player_image =pg.image.load (os.path.join(cwd,"pr/games/01_g/asset/enemies/enemy1.png"))
#agregar al grupo enemigo
enemies_group =pg.sprite.Group()
#crear enemigos
enemi_one = Enemies((300,300),enemy_image)
enemies_group.add(enemi_one)

#crear jugador o player
player_group =pg.sprite.Group()
player= Character((150,150),player_image)
player_group.add(player)
delta = 0
speed=300
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
    player_group.draw(screen)
    keys  = pg.key.get_pressed ()
    if keys[pg.K_d]or keys[pg.K_RIGHT]:
        player.move_x(speed*delta)
    if keys[pg.K_a]or keys[pg.K_LEFT]:
        player.move_left(speed*delta)
        pg.transform.flip(player_image,True,False)
    if keys[pg.K_w]or keys[pg.K_UP]:
        player.move_up(speed*delta)
    if keys[pg.K_s]or keys[pg.K_DOWN]:
        player.move_down(speed*delta)
    
    clock.tick(fps)
    delta = clock.tick(fps) / 1000
    #actualiozar la ventana 
    pg.display.flip()
pg.quit()