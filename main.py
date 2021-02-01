import random
import pygame

pygame.init()

# Creación de la pantalla de ejecución y colores
WIDTH = 1000
HEIGHT = 800
ventana = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fondo del juego
fondo = pygame.image.load('img/virus.jpg')
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))

fondoJugando = pygame.image.load('img/chip.jpg')
fondoJugando = pygame.transform.scale(fondoJugando, (WIDTH, HEIGHT))

# Título e icono
pygame.display.set_caption("Destruye Virus")
icon = pygame.image.load('img/mira.png')
pygame.display.set_icon(icon)

# Música del juego
file = 'music/retro.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.set_volume(0.009)
pygame.mixer.music.play(-1)  # If the loops is -1 then the music will repeat indefinitely.

# Forma del cursor
pygame.mouse.set_cursor(*pygame.cursors.broken_x)


# JUEGO


def ventPrincipal():
    pygame.init()

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    screen.blit(fondo, (0, 0))

    font = pygame.font.SysFont("serif", 60)
    text = font.render("Clica en la pantalla para empezar", True, BLACK)  # Texto
    center_x = (WIDTH // 2) - (text.get_width() // 2)  # Posición texto
    center_y = (HEIGHT // 2) - (text.get_height() // 2)
    screen.blit(text, [center_x, center_y])  # Ponerlo en pantalla

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            main()


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/gusano.png")
        self.image = pygame.transform.scale(self.image, (random.randrange(50, 70), random.randrange(50, 70)))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += random.randrange(1, 5)

        if self.rect.x > WIDTH:
            self.rect.x = -10
            self.rect.y = random.randrange(50, HEIGHT)


class Game(object):
    def __init__(self):
        self.game_over = False

        self.score = 0

        self.enemy_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        for i in range(50):
            enemy = Enemigo()
            enemy.rect.x = random.randrange(WIDTH)
            enemy.rect.y = random.randrange(50, HEIGHT)

            self.enemy_list.add(enemy)
            self.all_sprites_list.add(enemy)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

        return False

    def run_logic(self):
        if not self.game_over:
            self.all_sprites_list.update()

            # for event in pygame.event.get():
            #     if event.type == pygame.MOUSEBUTTONDOWN:
            #         sitioClicado = pygame.mouse.get_pos()
            #         if pygame.sprite.spritecollide(self.enemy_list, sitioClicado, True):
            #             print("Boom")

            # enemy_hit_list = pygame.sprite.spritecollide(self.player, self.meteor_list, True)

            # for enemy in enemy_hit_list:
            #     self.score += 1
            #     print("Llevas " + str(self.score) + " bajas de 50 enemigos")

            if len(self.enemy_list) == 0:
                self.game_over = True

    def display_frame(self, screen):
        screen.blit(fondo, (0, 0))

        if self.game_over:
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, Click Para Volver A Empezar", True, BLACK)  # Texto
            center_x = (WIDTH // 2) - (text.get_width() // 2)  # Posición texto
            center_y = (HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])  # Ponerlo en pantalla

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()


def main():
    pygame.init()

    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    done = False
    clock = pygame.time.Clock()

    game = Game()

    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)


pygame.quit()

if __name__ == "__main__":
    main()
