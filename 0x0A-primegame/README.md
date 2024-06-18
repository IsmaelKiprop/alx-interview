# 0x0A. Prime Game

## Description

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, this project involves determining who the winner of each game is.

## Requirements

- **Allowed editors:** vi, vim, emacs
- **Operating System:** Ubuntu 20.04 LTS
- **Python Version:** Python 3.4.3
- **Code Style:** PEP 8 (version 1.7.x)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/alx-interview.git
    ```

2. Navigate to the project directory:
    ```sh
    cd alx-interview/0x0A-primegame
    ```

## Usage

The project consists of a single Python file `0-prime_game.py` with a function `isWinner(x, nums)`.

### Function Prototype

```python
def isWinner(x, nums)
