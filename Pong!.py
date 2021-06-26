import pygame
import sys

WIDTH = 1366
HEIGHT = 768 - 60
FPS = 60

SCORE_1 = 0
SCORE_2 = 0

MAIN_COLOR = (240, 240, 240)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Bouncy!")
clock = pygame.time.Clock()

GAME_MODE = 0
boxy = HEIGHT / 2 + 200
start = True
while start:
    clock.tick(FPS)

    mouse = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    letters = pygame.font.Font(None, 50)
    letters2 = pygame.font.Font(None, 45)
    letters3 = pygame.font.Font(None, 100)
    startText = letters.render("Two Player", 1, MAIN_COLOR)
    single = letters2.render("Singleplayer", 1, MAIN_COLOR)
    LOGO = letters3.render("Pong!", 1, MAIN_COLOR)
    print(mouse)
    speed = 5
    isjump = True
    screen.fill((15, 15, 15))
    screen.blit(LOGO, (WIDTH / 2 - 100, 250))
    if 781 > mouse[0] > 583 and 628 > mouse[1] > 557:
        if mouse_press[0] == 1:
            GAME_MODE = 2
            start = False

        pygame.draw.rect(screen, (7, 7, 7), (WIDTH / 2 - 200 / 2, boxy, 200, 75))
        pygame.draw.rect(screen, (12, 12, 12), (WIDTH / 2 - 200 / 2, boxy, 195, 70))
        pygame.draw.rect(screen, (5, 5, 5), (WIDTH / 2 - 200 / 2, boxy - 100, 200, 75))
        pygame.draw.rect(screen, (10, 10, 10), (WIDTH / 2 - 200 / 2, boxy - 100, 195, 70))
        screen.blit(startText, (WIDTH / 2 - 200 / 2 + 10, boxy + 15))
        screen.blit(single, (WIDTH / 2 - 200 / 2 + 2, boxy + 13 - 100))
        pygame.display.update()
        pygame.display.flip()

    elif 781 > mouse[0] > 583 and 628 - 100 > mouse[1] > 557 - 100:
        if mouse_press[0] == 1:
            GAME_MODE = 1
            start = False
        pygame.draw.rect(screen, (5, 5, 5), (WIDTH / 2 - 200 / 2, boxy, 200, 75))
        pygame.draw.rect(screen, (10, 10, 10), (WIDTH / 2 - 200 / 2, boxy, 195, 70))
        pygame.draw.rect(screen, (7, 7, 7), (WIDTH / 2 - 200 / 2, boxy - 100, 200, 75))
        pygame.draw.rect(screen, (12, 12, 12), (WIDTH / 2 - 200 / 2, boxy - 100, 195, 70))
        screen.blit(startText, (WIDTH / 2 - 200 / 2 + 10, boxy + 15))
        screen.blit(single, (WIDTH / 2 - 200 / 2 + 2, boxy + 13 - 100))
        pygame.display.update()
        pygame.display.flip()
    else:
        pygame.draw.rect(screen, (5, 5, 5), (WIDTH / 2 - 200 / 2, boxy, 200, 75))
        pygame.draw.rect(screen, (10, 10, 10), (WIDTH / 2 - 200 / 2, boxy, 195, 70))

        pygame.draw.rect(screen, (5, 5, 5), (WIDTH / 2 - 200 / 2, boxy - 100, 200, 75))
        pygame.draw.rect(screen, (10, 10, 10), (WIDTH / 2 - 200 / 2, boxy - 100, 195, 70))

    screen.blit(startText, (WIDTH / 2 - 200 / 2 + 10, boxy + 15))
    screen.blit(single, (WIDTH / 2 - 200 / 2 + 2, boxy + 13 - 100))
    pygame.display.update()
    pygame.display.flip()


class Player1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 90))
        self.image.fill(MAIN_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 5

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.rect.y -= self.vel

        if key[pygame.K_s]:
            self.rect.y += self.vel

        if self.rect.top <= 0:
            self.rect.y += self.vel

        if self.rect.bottom >= HEIGHT:
            self.rect.y -= self.vel


class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 90))
        self.image.fill(MAIN_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 5

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            self.rect.y -= self.vel

        if key[pygame.K_DOWN]:
            self.rect.y += self.vel

        if self.rect.top <= 0:
            self.rect.y += self.vel

        if self.rect.bottom >= HEIGHT:
            self.rect.y -= self.vel


class Bot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 90))
        self.image.fill(MAIN_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 5
        self.reset = False
        self.destination = 0

    def update(self):
        self.destination = ball.rect.y

        print(str(self.rect.y) + " " + str(self.destination))

        if ball.rect.x >= WIDTH / 2:
            if ball.velx == -5:
                pass
            else:
                if self.rect.y < self.destination:
                    self.rect.y += self.vel
                elif self.rect.y > self.destination:
                    self.rect.y -= self.vel

        if self.rect.top <= 0:
            self.rect.y += self.vel

        if self.rect.bottom >= HEIGHT:
            self.rect.y -= self.vel


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill(MAIN_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.velx = 5
        self.vely = 5

    def update(self):

        hit1 = pygame.sprite.spritecollide(player1, balls, False)
        if GAME_MODE == 2:
            hit2 = pygame.sprite.spritecollide(player2, balls, False)
        else:
            hit2 = pygame.sprite.spritecollide(bot, balls, False)

        if hit1 or hit2:
            self.velx = -self.velx

        self.rect.x += self.velx
        self.rect.y += self.vely

        if self.rect.right >= WIDTH:
            self.velx = -self.velx
            global SCORE_1
            SCORE_1 += 1

        if self.rect.left <= 0:
            self.velx = -self.velx
            global SCORE_2
            SCORE_2 += 1

        if self.rect.top <= 0:
            self.vely = -self.vely

        if self.rect.bottom >= HEIGHT:
            self.vely = -self.vely


all_sprites = pygame.sprite.Group()
if GAME_MODE == 2:
    player1 = Player1(10, HEIGHT / 2)
    player2 = Player2(WIDTH - 20, HEIGHT / 2)
    ball = Ball()
    balls = pygame.sprite.Group()
    balls.add(ball)
    all_sprites.add(player1)
    all_sprites.add(player2)
    all_sprites.add(ball)
else:
    player1 = Player1(10, HEIGHT / 2)
    bot = Bot(WIDTH - 20, HEIGHT / 2)
    ball = Ball()
    balls = pygame.sprite.Group()
    balls.add(ball)
    all_sprites.add(player1)
    all_sprites.add(bot)
    all_sprites.add(ball)

run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((15, 15, 15))
    all_sprites.draw(screen)
    all_sprites.update()

    score_letters = pygame.font.Font(None, 25)
    SCORE_TEXT_1 = score_letters.render("SCORE:" + str(SCORE_1), 1, MAIN_COLOR)
    SCORE_TEXT_2 = score_letters.render("SCORE:" + str(SCORE_2), 1, MAIN_COLOR)
    screen.blit(SCORE_TEXT_1, (0, 0))
    screen.blit(SCORE_TEXT_2, (WIDTH - 75, 0))
    pygame.display.update()
    pygame.display.flip()

pygame.quit()
