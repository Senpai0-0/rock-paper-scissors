# Rock Paper Scissors (CLI)

A simple command-line Rock Paper Scissors game written in Python. This project was built as a beginner-friendly exercise covering core Python concepts: functions, conditionals, loops, and dictionaries.

## How It Works

- You play against the computer in the terminal.
- Choose `tas` (rock), `kagit` (paper), or `makas` (scissors).
- The computer picks randomly, and the winner is decided using classic Rock Paper Scissors rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
- Play continues in a loop until you type `q` to quit.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Senpai0-0/rock-paper-scissors.git
   cd rock-paper-scissors-cli
   ```

2. Run the game:
   ```bash
   python tas_kagit_makas.py
   ```

## Example Gameplay

```
=== TAŞ KAĞIT MAKAS ===
Seçenekler: tas, kagit, makas (çıkmak için 'q')

Seçimin: tas
Sen: tas | Bilgisayar: makas
Sonuç: Kazandın!

Seçimin: q
Oyun bitti, görüşürüz!
```

## Project Structure

```
rock-paper-scissors-cli/
├── tas_kagit_makas.py   # Main game logic
└── README.md
```

## Concepts Covered

- Using the `random` module for computer choices
- Dictionaries for clean win/lose logic (instead of long if/elif chains)
- Input validation and string handling
- Loops for continuous gameplay

## Possible Improvements

- [ ] Add a score tracker (wins/losses/ties)
- [ ] Add a graphical version using `pygame`
- [ ] Support best-of-N rounds
- [ ] Add unit tests
