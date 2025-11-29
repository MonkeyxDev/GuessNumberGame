# 🎯 Guess Number Game

A modern and interactive number guessing game built with **Python** and **CustomTkinter**.  
This game challenges the player to guess a random number between 1 and 100 with limited attempts based on the selected difficulty.

## 🚀 Features
- ✔️ Modern GUI with CustomTkinter  
- ✔️ Difficulty levels: Easy / Normal / Hard  
- ✔️ Random number generation  
- ✔️ Hint system (Higher / Lower)  
- ✔️ Light & Dark mode  
- ✔️ Restart / New Game system  
- ✔️ Clean and simple UI


## 🛠️ Installation & Running

### 1️⃣ Clone the repository
git clone https://github.com/MonkeyxDev/GuessNumberGame.git

### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Run the game
python src/game.py


## 📦 Requirements
- Python 3.13  
- customtkinter


## 🔧 Difficulty System
| Difficulty | Attempts |
|-----------|----------|
| Easy      | 20       |
| Normal    | 15       |
| Hard      | 7        |


## 🧩 How the Game Works
- The program randomly selects a number between **1 and 100**.
- The player must guess the secret number using the input field.
- Based on the selected difficulty, the player has a limited number of attempts.
- After each guess, the game provides a hint:
  - **Higher** → The secret number is greater than your guess.
  - **Lower** → The secret number is smaller than your guess.
- If the player guesses the number, they win the game.
- If attempts reach zero, the game ends with a loss message.
- A new game can be started anytime by clicking **New Game**.

 
## 📜 License
This project is licensed under the **MIT License**.  
Feel free to use, modify, or distribute the source code.


## ⭐ Support
If you enjoyed this project, consider giving it a ⭐ star on GitHub — it really helps and motivates further development!
