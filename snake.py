#snake game using pygame
import pygame
import sys
import random

pygame.init()

SW, SH = 800, 800

BLOCK_SIZE = 50

FONT = pygame.font.Font("freesansbold.ttf", BLOCK_SIZE*2)

screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.size = 1
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.death = False
        self.xdir, self.ydir = 1, 0

    def move(self):
        self.body.append(self.head)
        if self.death:
            return
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.body[0])
        

def draw_grid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)

draw_grid()

snake = Snake()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.xdir, snake.ydir = 0, -1
            if event.key == pygame.K_DOWN:
                snake.xdir, snake.ydir = 0, 1
            if event.key == pygame.K_LEFT:
                snake.xdir, snake.ydir = -1, 0
            if event.key == pygame.K_RIGHT:
                snake.xdir, snake.ydir = 1, 0

    snake.move()

    screen.fill((0, 0, 0))
    draw_grid()

    pygame.draw.rect(screen, (0, 255, 0), snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, (0, 255, 0), square)

    pygame.display.flip()
    clock.tick(5)

