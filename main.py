import pygame, fuentes, juego, conexion, ventana

#Iniciar pygame
pygame.init()

#Creación de la pantalla de ejecución
WIDTH = 1000
HEIGHT = 800
ventana = pygame.display.set_mode((WIDTH,HEIGHT))

#Fondo del juego
fondo = pygame.image.load('img/virus.jpg')
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))

#Título e icono
pygame.display.set_caption("Destruye Virus")
icon = pygame.image.load('img/mira.png')
pygame.display.set_icon(icon)

#Música del juego
file = 'music/retro.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.set_volume(0.009)
pygame.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.

#Forma del cursor
pygame.mouse.set_cursor(*pygame.cursors.broken_x)


#loop del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ventana.blit(fondo, (0, 0))
    ventana.blit(fuentes.Fuentes.texto, fuentes.Fuentes.tr1)
    ventana.blit(fuentes.Fuentes.texto2, fuentes.Fuentes.tr2)
    pygame.display.update()