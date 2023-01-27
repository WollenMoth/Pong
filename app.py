import pygame

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

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        rect = (self.x, self.y, BAR_WIDTH, BAR_HEIGHT)
        pygame.draw.rect(screen, self.COLOR, rect)

    def move(self, up=True):
        if up:
            self.y = max(self.y - self.VEL, 0)
        else:
            self.y = min(self.y + self.VEL, HEIGHT - BAR_HEIGHT)


def draw(screen: pygame.Surface, bars: tuple[Bar, ...]):
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


def main():
    running = True
    clock = pygame.time.Clock()

    bar_center = (HEIGHT - BAR_HEIGHT) // 2
    bar_right = WIDTH - BAR_WIDTH - BAR_OFFSET

    left_bar = Bar(BAR_OFFSET, bar_center)
    right_bar = Bar(bar_right, bar_center)

    bars = (left_bar, right_bar)

    while running:
        clock.tick(FPS)

        draw(screen, bars)

        keys = pygame.key.get_pressed()
        handle_bar_movement(keys, bars)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()
