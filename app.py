import pygame
import random

WIDTH, HEIGHT = 800, 600

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BAR_WIDTH = 16
BAR_HEIGHT = HEIGHT // 5
BAR_OFFSET = BAR_WIDTH

LINE_WIDTH = 10
LINE_NUMBER = 20

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pong")


class Bar:
    COLOR = WHITE
    VEL = 5
    WIDTH = BAR_WIDTH
    HEIGHT = BAR_HEIGHT

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        rect = (self.x, self.y, self.WIDTH, self.HEIGHT)
        pygame.draw.rect(screen, self.COLOR, rect)

    def move(self, up=True):
        if up:
            self.y = max(self.y - self.VEL, 0)
        else:
            self.y = min(self.y + self.VEL, HEIGHT - BAR_HEIGHT)


class Ball:
    COLOR = WHITE
    RADIUS = 10
    VEL_X = random.randint(-4, 4)
    VEL_Y = random.randint(-4, 4)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, self.COLOR, (self.x, self.y), self.RADIUS)

    def move(self):
        self.x += self.VEL_X
        self.y += self.VEL_Y

    def check(self, screen):
        if (self.x - self.RADIUS <= 0 or self.x + self.RADIUS >= screen.get_width()):
            self.VEL_X *= -1

        if (self.y - self.RADIUS <= 0 or self.y + self.RADIUS >= screen.get_height()):
            self.VEL_Y *= -1


def draw(screen: pygame.Surface, bars: tuple[Bar, ...], ball: Ball):
    screen.fill(BLACK)

    for bar in bars:
        bar.draw(screen)

    line_step = HEIGHT // LINE_NUMBER
    line_center = (WIDTH - LINE_WIDTH) // 2

    for i in range(line_step // 2, HEIGHT, line_step):
        if i // (line_step) % 2:
            continue

        rect = (line_center, i, LINE_WIDTH, line_step)
        pygame.draw.rect(screen, WHITE, rect)

    ball.draw(screen)

    pygame.display.flip()


def handle_bar_movement(keys, bars: tuple[Bar, ...]):
    left_bar, right_bar = bars

    if keys[pygame.K_w]:
        left_bar.move()
    elif keys[pygame.K_s]:
        left_bar.move(up=False)

    if keys[pygame.K_UP]:
        right_bar.move()
    elif keys[pygame.K_DOWN]:
        right_bar.move(up=False)


def handle_ball_movement(screen, ball: Ball):
    ball.move()
    ball.check(screen)


def main():
    running = True
    clock = pygame.time.Clock()

    bar_center = (HEIGHT - BAR_HEIGHT) // 2
    bar_right = WIDTH - BAR_WIDTH - BAR_OFFSET

    left_bar = Bar(BAR_OFFSET, bar_center)
    right_bar = Bar(bar_right, bar_center)

    bars = (left_bar, right_bar)

    ball = Ball(WIDTH // 2, HEIGHT // 2)

    while running:
        clock.tick(FPS)

        draw(screen, bars, ball)

        keys = pygame.key.get_pressed()

        handle_bar_movement(keys, bars)

        handle_ball_movement(screen, ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()
