# Snake Game with Reinforcement Learning

https://github.com/ananthanarayanan-25/ml-projects/assets/Screen%20Recording.mp4

## Overview
AI learns to play Snake using Q-Learning reinforcement learning algorithm.

## Installation
```bash
pip install pygame
```

## Usage
Train the AI:
```bash
python q_learning.py
```

Watch the trained AI play:
```bash
python play_snake_ai.py
```

## How It Works
- **Environment**: 20x15 grid
- **Algorithm**: Q-Learning
- **State**: 8 features (food direction + danger detection)
- **Actions**: Right, Down, Left, Up
- **Rewards**: +10 food, -10 death, -0.1 per step

## Files
- `snake_env.py` - RL environment
- `q_learning.py` - Training script
- `play_snake_ai.py` - Visualization
- `q_table.pkl` - Trained model (generated after training)
