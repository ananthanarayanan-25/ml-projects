import random

class SnakeEnv:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = 0
        self.food = self._spawn_food()
        self.steps = 0
        return self._get_state()

    def _spawn_food(self):
        while True:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food not in self.snake:
                return food

    def _get_state(self):
        head = self.snake[0]
        fx, fy = self.food
        return (
            head[0] < fx,
            head[0] > fx,
            head[1] < fy,
            head[1] > fy,
            self._danger(0),
            self._danger(1),
            self._danger(2),
            self._danger(3)
        )

    def _danger(self, action):
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dx, dy = dirs[action]
        x, y = self.snake[0]
        nx, ny = x + dx, y + dy
        return nx < 0 or nx >= self.width or ny < 0 or ny >= self.height or (nx, ny) in self.snake

    def step(self, action):
        self.direction = action
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dx, dy = dirs[action]
        head = self.snake[0]
        new_head = (head[0] + dx, head[1] + dy)

        if new_head[0] < 0 or new_head[0] >= self.width or new_head[1] < 0 or new_head[1] >= self.height:
            return self._get_state(), -10, True

        if new_head in self.snake:
            return self._get_state(), -10, True

        self.snake.insert(0, new_head)

        if new_head == self.food:
            reward = 10
            self.food = self._spawn_food()
        else:
            self.snake.pop()
            reward = -0.1

        self.steps += 1
        if self.steps > 100 * len(self.snake):
            return self._get_state(), -10, True

        return self._get_state(), reward, False
