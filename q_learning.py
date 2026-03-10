from snake_env import SnakeEnv
import random
from collections import defaultdict
import pickle

# ENV
env = SnakeEnv()

# Q-table
Q = defaultdict(lambda: [0, 0, 0, 0])

# Hyperparameters
alpha = 0.1        # learning rate
gamma = 0.9        # discount factor
epsilon = 1.0      # exploration
epsilon_decay = 0.995
epsilon_min = 0.01

episodes = 5000

for episode in range(episodes):
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        # ε-greedy action selection
        if random.random() < epsilon:
            action = random.randint(0, 3)
        else:
            action = Q[state].index(max(Q[state]))

        next_state, reward, done = env.step(action)
        total_reward += reward

        # Q-learning update
        best_next = max(Q[next_state])
        Q[state][action] += alpha * (reward + gamma * best_next - Q[state][action])

        state = next_state

    # decay exploration
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    if episode % 500 == 0:
        print(f"Episode {episode}, reward = {total_reward:.2f}, epsilon = {epsilon:.3f}")

print("Training finished")

with open('q_table.pkl', 'wb') as f:
    pickle.dump(dict(Q), f)
print("Model saved to q_table.pkl")
