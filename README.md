# Rock Paper Scissors Game
## Description
This program emulates the classic Rock, Paper, Scissors game. It allows a user to play against the computer in an interactive and fun way. The program also includes graphical representations of the choices (`rock`, `paper`, and `scissors`), enhancing the user experience.

---

## Features
* User-friendly interface to select between Rock, Paper, or Scissors.
* The computer randomly selects its choice to compete against the user.
* Clear instructions and error handling for invalid inputs.
* Option to replay the game after each round.
* Terminal screen is cleared between rounds for a seamless experience.

---

## Prerequisites
To run the program, ensure you have the following:
* Python 3.x installed on your system.
* A `data.py` file in the same directory containing ASCII art for:
  * rock
  * paper
  * scissors

Example structure of data.py:

```python
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
```

---

## How to Run
1. Clone or download the script and data.py file to a directory.
2. Open a terminal and navigate to the directory containing the files.
3. Run the script with the command:

    ```shell
    python3 rock_paper_scissors.py
    ```

---

## How to Play
1. Choose your move:
    * 0 for Rock
    * 1 for Paper
    * 2 for Scissors
2. The program will display both your choice and the computer's choice.
3. Results will be displayed based on the rules:
   * Rock beats Scissors
   * Scissors beats Paper
   * Paper beats Rock
4. After each round, you can choose to:
   * Play again by typing Y
   * Exit the game by typing N

---

## Example Gameplay
```
WELCOME TO ROCK PAPER SCISSORS!!!
What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: 0
You chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

You lose!
Would you like to play again? Type 'Y' for yes, 'N' for no: N
```

---

## Future Enhancements
* Add scoring to track wins, losses, and draws over multiple rounds.
* Introduce a multiplayer option.
* Enhance with a graphical user interface (GUI).
* Allow more choices like Lizard and Spock for extended gameplay.

---

## License
This program is open-source and can be freely modified or distributed. Have fun coding! 🚀
