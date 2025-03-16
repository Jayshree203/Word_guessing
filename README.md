# Word Guessing Game

A simple command-line word guessing game built with Python. Players have to guess a word one letter at a time, with a limited number of attempts.

## Features
- Random word selection from a predefined list
- 12 attempts to guess the word
- Interactive command-line interface
- Player name customization

## Requirements
- Python 3.x

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/word-guess.git
cd word-guess
```

2. No additional packages are required as the game uses only Python standard library.

## How to Run

Run the game using Python:
```bash
python word.py
```

## How to Play
1. When prompted, enter your name
2. The game will select a random word and show it as underscores (_)
3. Guess one letter at a time
4. You have 12 attempts to guess the word correctly
5. For each correct guess, the letter will be revealed in its correct position(s)
6. For each wrong guess, you lose one attempt
7. Win by guessing all letters in the word before running out of attempts

## Project Structure
```
word-guess/
├── word.py           # Main game file
├── requirements.txt  # Project dependencies (empty)
└── README.md        # This file
``` 