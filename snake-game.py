import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake - Grid Aligned")

clock = pygame.time.Clock()
block_size = 20
speed = block_size

snake = [(200, 140)] 
dx, dy = 0, 0

def get_random_food():
    return (
        random.randrange(0, WIDTH - block_size, block_size),
        random.randrange(0, HEIGHT - block_size, block_size)
    )

food_x, food_y = get_random_food()

running = True
while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dx, dy = 0, -speed
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, speed
            elif event.key == pygame.K_LEFT:
                dx, dy = -speed, 0
            elif event.key == pygame.K_RIGHT:
                dx, dy = speed, 0

    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT
    ):
        print("Wall hit! Game over.")
        break

    if new_head in snake[1:]:
        print("Self collision! Game over.")
        break

    snake.insert(0, new_head)

    if new_head == (food_x, food_y):
        print("Food eaten 🍎")
        food_x, food_y = get_random_food()
    else:
        snake.pop()  

    screen.fill((0, 0, 0))
    for block in snake:
        pygame.draw.rect(
            screen, (0, 255, 0),
            (block[0], block[1], block_size, block_size)
        )

    pygame.draw.rect(
        screen, (255, 0, 0),
        (food_x, food_y, block_size, block_size)
    )

    pygame.display.update()

pygame.quit()