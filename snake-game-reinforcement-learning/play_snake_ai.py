import pygame
from snake_env import SnakeEnv
import pickle

with open('q_table.pkl', 'rb') as f:
    Q = pickle.load(f)

env = SnakeEnv()
pygame.init()

block_size = 20
screen = pygame.display.set_mode((env.width * block_size, env.height * block_size))
pygame.display.set_caption("Snake AI Playing")
clock = pygame.time.Clock()

state = env.reset()
running = True

while running:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    action = Q.get(state, [0, 0, 0, 0])
    action = action.index(max(action))
    
    state, reward, done = env.step(action)
    
    if done:
        print(f"Game Over! Score: {len(env.snake) - 1}")
        state = env.reset()
    
    screen.fill((0, 0, 0))
    
    for segment in env.snake:
        pygame.draw.rect(screen, (0, 255, 0), 
                        (segment[0] * block_size, segment[1] * block_size, block_size, block_size))
    
    pygame.draw.rect(screen, (255, 0, 0), 
                    (env.food[0] * block_size, env.food[1] * block_size, block_size, block_size))
    
    pygame.display.update()

pygame.quit()
