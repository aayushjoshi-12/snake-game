# Snake Game with AI

Welcome to the Snake Game with AI, a Python project that combines the classic arcade game with artificial intelligence. This project presents a modern twist on the traditional Snake game by incorporating an AI agent that learns to navigate the game environment through reinforcement learning.

## Features

- Classic Snake gameplay with intuitive controls.
- AI mode challenges the player by automatically navigating the snake.
- Customizable game settings, including speed and size.
- Score tracking and display.
- Real-time plotting of scores and mean scores during training for immediate feedback.

## Installation

1. Ensure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).
2. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/aayushjoshi-12/Snake_Game.git
   ```

3. Navigate to the project directory:

   ```bash
   cd Snake_Game
   ```

4. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To play the game manually:

```bash
python snake_game.py
```

To train the AI agent:

```bash
python agent.py
```

## Folder Structure

- `model/`: Contains the saved model weights (`model.pth`).
- `Arial.ttf`: Font file for text rendering.
- `agent.py`: Script for training the AI agent.
- `game.py`: Contains the main game logic.
- `helper.py`: Helper script for plotting training progress.
- `model.py`: Defines the neural network architecture and training process.
- `requirements.txt`: Lists the dependencies required to run the project.
- `readme.md`: This file, providing information about the project.

## Neural Network Model

The AI agent in this project employs a simple yet effective neural network architecture known as the Q-network. This network consists of a single hidden layer followed by an output layer, where the input represents the current state of the game, and the output represents the Q-values corresponding to each possible action.

The Q-network is implemented using PyTorch, a popular deep learning framework in Python. During training, the agent learns to approximate the optimal action-value function, which guides its decision-making process in the game environment.

For more details on the neural network architecture and training process, please refer to the `model.py` file.

## Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to help improve this project.

## Contact Information

For any inquiries or support, please contact [Aayush Joshi](mailto:joshiaayush1244@gmail.com).
