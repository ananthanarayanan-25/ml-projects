# ml-projects
Machine learning projects including regression, classification and experiments using Python.

---

## Snake Game with Reinforcement Learning

https://github.com/user-attachments/assets/your-video-id-here

### Overview
AI learns to play Snake using Q-Learning reinforcement learning algorithm.

### Installation
```bash
pip install pygame
```

### Usage
Train the AI:
```bash
python q_learning.py
```

Watch the trained AI play:
```bash
python play.py
```

### How It Works
- **Environment**: 20x15 grid
- **Algorithm**: Q-Learning
- **State**: 8 features (food direction + danger detection)
- **Actions**: Right, Down, Left, Up
- **Rewards**: +10 food, -10 death, -0.1 per step

### Files
- `snake_env.py` - RL environment
- `q_learning.py` - Training script
- `play.py` - Visualization
- `q_table.pkl` - Trained model (generated after training)
