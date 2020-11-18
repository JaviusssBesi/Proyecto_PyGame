import pygame

'''
Iniciar de pygame
'''
pygame.init()

#Creación de la pantalla de ejecución
WIDTH = 800
HEIGHT = 600
ventana = pygame.display.set_mode((WIDTH,HEIGHT))
fondo = pygame.image.load('img/virus.jpg')
picture = pygame.transform.scale(fondo, (800, 600))

#Título e icono
pygame.display.set_caption("Destruye Virus")
icon = pygame.image.load('img/mira.png')
pygame.display.set_icon(icon)

#Música del juego
file = 'music/retro.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.set_volume(0.008)
pygame.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.

#Forma del cursor
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

#Textos del juego
AMARILLO = (255, 255, 0)
AZUL = (0, 0, 255)
fuente= pygame.font.Font(None,50)
texto = fuente.render("Virus Destroyer",0, AZUL)
text_rect = texto.get_rect(center=(WIDTH/2, HEIGHT/2))

#loop del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ventana.blit(fondo, (0, 0))
    ventana.blit(texto, text_rect)
    pygame.display.update()

class Main():
    def __init__(self):





if __name__ == '__main__':
    window = Main()