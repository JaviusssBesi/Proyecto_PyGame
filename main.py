#Hecho por: Javier Besada y Oscar Blanco

import pygame, random

pygame.init()

# Tamaño de pantalla
ANCHO = 800
ALTO = 600

# Inicialización de Pygame, creación de la ventana, título y control de reloj.
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()
FPS = 30

# Paleta de colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Fondo del juego
fondo = pygame.image.load('img/virus.jpg')
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

fondoJugando = pygame.image.load('img/chip.jpg')
fondoJugando = pygame.transform.scale(fondoJugando, (ANCHO, ALTO))

start = pygame.transform.scale(pygame.image.load('img/start.png').convert(), (70, 70))
start.set_colorkey(BLANCO)
stop = pygame.transform.scale(pygame.image.load('img/stop.png').convert(), (70, 70))
stop.set_colorkey(BLANCO)
reinicio = pygame.transform.scale(pygame.image.load('img/reinicio.png').convert(), (70, 70))
reinicio.set_colorkey(NEGRO)
acercade = pygame.transform.scale(pygame.image.load('img/acercade.png').convert(), (35, 35))
acercade.set_colorkey(BLANCO)
acercade.set_colorkey(NEGRO)

# Título e icono
pygame.display.set_caption("Destruye Virus")
icon = pygame.image.load('img/mira.png')
pygame.display.set_icon(icon)

#Fuentes
consolas = pygame.font.match_font('consolas')
times = pygame.font.match_font('times')
arial = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')

# Música del juego
file = 'music/retro.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.set_volume(0.009)
pygame.mixer.music.play(-1)


# JUEGO

class VentanaPrincipal():
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/virus.jpg').convert(), (ANCHO, ALTO))
        pantalla.blit(self.image, (0, 0))

        muestra_texto(pantalla, times, '¿Quieres Jugar?', NEGRO, 60, ANCHO // 2, 300)

        inicio
        salida

        muestra_texto(pantalla, times, 'Iniciar', NEGRO, 15, ANCHO // 2 - 150, 480)
        muestra_texto(pantalla, times, 'Salir', NEGRO, 15, ANCHO // 2 + 150, 480)
        muestra_texto(pantalla, times, 'Acerca de', ROJO, 15, 42, 70)

class Boton():
    def __init__(self, x, y, image):
         self.image = image
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         self.clicked = False

    def draw(self):
        clicado = False

        posicion = pygame.mouse.get_pos()

        if self.rect.collidepoint(posicion):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                clicado = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
             self.clicked = False

        pantalla.blit(self.image, self.rect)

        return clicado

inicio = Boton(ANCHO // 2 - 185, 400, start)
salida = Boton(ANCHO // 2 + 115, 400, stop)
reinicio = Boton(ANCHO // 2 - 185, 400, reinicio)
acercade = Boton(25, 25, acercade)

class ObjetoJugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/mira.png").convert()
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.radius = 16

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]

class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_aleatoria = random.randrange(4)

        if self.img_aleatoria == 0:
            self.image = pygame.transform.scale(pygame.image.load('img/enemigo.png').convert(), (35, 35))
            self.radius = 22
        if self.img_aleatoria == 1:
            self.image = pygame.transform.scale(pygame.image.load('img/enemigo2.png').convert(), (35, 40))
            self.radius = 22
        if self.img_aleatoria == 2:
            self.image = pygame.transform.scale(pygame.image.load('img/enemigo3.png').convert(), (35, 35))
            self.radius = 22
        if self.img_aleatoria == 3:
            self.image = pygame.transform.scale(pygame.image.load('img/enemigo4.png').convert(), (40, 35))
            self.radius = 22

        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - 70)

        self.velocidad_x = random.randrange(8, 11) * random.randrange(-1, 2)
        self.velocidad_y = random.randrange(8, 11)

    def update(self):
        # Actualiza la velocida/posición del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocidad_x += 1
        # Limita el margen derecho
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        # Limita el margen de arriba
        if self.rect.top < 70:
            self.velocidad_y += 1
        # Limita el margen de abajo
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1



def muestra_texto(pantalla, fuente, texto, color, dimensiones, x, y):
    tipo_letra = pygame.font.Font(fuente, dimensiones)
    superficie = tipo_letra.render(texto, True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    pantalla.blit(superficie, rectangulo)

# Grupo de sprites
jugadores = pygame.sprite.Group()
enemigos = pygame.sprite.Group()

#Instanciaciones
ventana = VentanaPrincipal()

jugador = ObjetoJugador()
jugadores.add(jugador)

numero_enem = 32

for x in range(numero_enem):
    enemigo = Enemigos()
    enemigos.add(enemigo)

#Variables
tiempo = 0
matados = 1
punt_max = 0
menu_inicial = True
game_over = 1
cadencia = 1000
actualizacion = pygame.time.get_ticks()


# Bucle de juego
ejecutando = True
while ejecutando:
    # Es lo que especifica la velocidad del bucle de juego
    clock.tick(FPS)
    # Eventos
    for event in pygame.event.get():
        # Se cierra y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False

    # Ventana Principal
    ventana

    if menu_inicial == True:
        if salida.draw():
            ejecutando = False
        if inicio.draw():
            menu_inicial = False
        if acercade.draw():
            pantalla.blit(fondo, (0, 0))
            muestra_texto(pantalla, arial, 'Este juego está creado por:', BLANCO, 30, ANCHO // 2, 95)
            muestra_texto(pantalla, arial, 'Javier Besada Perez', BLANCO, 30, ANCHO // 2, 140)
            muestra_texto(pantalla, arial, 'Oscar Blanco Lorenzo', BLANCO, 30, ANCHO // 2, 170)

            muestra_texto(pantalla, arial, 'Consiste en eliminar todos los virus', BLANCO, 30, ANCHO // 2, 230)
            muestra_texto(pantalla, arial, 'que amenazan nuestro ordenador.', BLANCO, 30, ANCHO // 2, 260)
            muestra_texto(pantalla, arial, '¿Te atreves?', BLANCO, 30, ANCHO // 2, 320)

    else:
        if game_over != 0:
            #Fondo de pantalla
            pantalla.blit(fondoJugando, (0, 0))

            #Desaparecer cursor
            pygame.mouse.set_visible(0)

            # Actualización de sprites
            jugadores.update()
            enemigos.update()

            colision = pygame.sprite.spritecollide(jugador, enemigos, True, pygame.sprite.collide_circle)

            if colision:
                print('Has alcanzado ' + str(matados) + ' enemigos')
                matados += 1

            #Para que sigan saliendo los enemigos
            for y in range(3):
                if not enemigos:
                    numero_enem -= 5
                    for z in range(numero_enem):
                        enemigo = Enemigos()
                        enemigos.add(enemigo)

            #Dibujo de sprites.
            jugadores.draw(pantalla)
            enemigos.draw(pantalla)

            #Contador
            muestra_texto(pantalla, arial, str(tiempo), ROJO, 20, ANCHO // 2, 30)
            ahora = pygame.time.get_ticks()
            if ahora - actualizacion > cadencia:
                tiempo += 1
                actualizacion = ahora

            #Puntuacion A Batir
            muestra_texto(pantalla, consolas, 'Punt. A Batir: ' + str(punt_max), ROJO, 20, 700, 30)

            #Game Over
            if matados == 101:
                game_over = 0
                pygame.mouse.set_visible(1)
                print('Muy buena partida!! Has eliminado 100 enemigos en ' + str(tiempo) + ' segundos.')

                punt_max = tiempo

        elif game_over == 0:
            pantalla.blit(fondo, (0, 0))
            muestra_texto(pantalla, consolas, '¿Quieres volver a intentarlo?', NEGRO, 50, ANCHO // 2, 300)
            reinicio
            salida
            muestra_texto(pantalla, times, 'Reiniciar', NEGRO, 15, ANCHO // 2 - 150, 480)
            muestra_texto(pantalla, times, 'Salir', NEGRO, 15, ANCHO // 2 + 150, 480)

            if salida.draw():
                ejecutando = False

            if reinicio.draw():
                tiempo = 0
                numero_enem = 40
                matados = 1
                game_over = 1

                # Fondo de pantalla
                pantalla.blit(fondoJugando, (0, 0))

                # Desaparecer cursor
                pygame.mouse.set_visible(0)

                # Actualización de sprites
                jugadores.update()
                enemigos.update()

                colision = pygame.sprite.spritecollide(jugador, enemigos, True, pygame.sprite.collide_circle)

                if colision:
                    print('Has alcanzado ' + str(matados) + ' enemigos')
                    matados += 1

                # Para que sigan saliendo los enemigos
                for y in range(3):
                    if not enemigos:
                        numero_enem -= 10
                        for z in range(numero_enem):
                            enemigo = Enemigos()
                            enemigos.add(enemigo)

                # Dibujo de sprites.
                jugadores.draw(pantalla)
                enemigos.draw(pantalla)

                # Contador
                muestra_texto(pantalla, arial, str(tiempo), ROJO, 20, ANCHO // 2, 30)
                ahora = pygame.time.get_ticks()
                if ahora - actualizacion > cadencia:
                    tiempo += 1
                    actualizacion = ahora

                #Puntuacion A Batir
                muestra_texto(pantalla, consolas, 'Punt. A Batir: ' + str(punt_max), ROJO, 20, 700, 30)

                # Game Over
                if matados == 101:
                    game_over = 0
                    pygame.mouse.set_visible(1)
                    print('Muy buena partida!! Has eliminado 100 enemigos en ' + str(tiempo) + ' segundos.')

                    punt_max = tiempo

    # Actualiza el contenido de la pantalla.
    pygame.display.flip()

pygame.quit()