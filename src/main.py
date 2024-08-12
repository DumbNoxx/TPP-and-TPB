#Importamos la libreria
import pygame

#Creamos el tamaño de la ventana
pygame.init()
pantalla = pygame.display.set_mode((800,600))
reloj = pygame.time.Clock()
running = True

# titulo e icono
pygame.display.set_caption('Tu pana burger')
icon = pygame.image.load("/media/dylan/Nuevo vol/pc/Documents/programacion/python/Juego de  la panaderia/resources/icons/icon.png")
pygame.display.set_icon(icon)

# * Colocar mi jugador
playerDefaultMan = pygame.image.load("/media/dylan/Nuevo vol/pc/Documents/programacion/python/Juego de  la panaderia/resources/players/default_player_man.png")
playerx = 400
playery = 300
dt = 0

def Player():
    pantalla.blit(playerDefaultMan,(playerx,playery))

# * Juego
while running:
    pantalla.fill(('gray'))

    # * Creamos el evento para cerrar por el boton X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # * Codigo del juego
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    if keys[pygame.K_w]:
        playery -= 300 * dt
    if keys[pygame.K_s]:
        playery += 300 * dt
    if keys[pygame.K_a]:
        playerx -= 300 * dt
    if keys[pygame.K_d]:
        playerx += 300 * dt


    # * Nuestras funciones,etc, para mostrar en pantalla
    Player()
    pygame.display.update()

    pygame.display.flip()

    dt = reloj.tick(60) / 1000

pygame.quit()