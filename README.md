# Wordle Clone
A terminal-based clone of the popular NY Times game Wordle, built in Python and styled using the Rich library for coloured and formatted output.

---

## 🎮 Game Features
- Guess the 5-letter hidden word in **6 attempts**
- Colour-coded feedback:
  - 🟩 Green (Correct letter, correct position)
  - 🟨 Yellow (Correct letter, incorrect position)
  - ⬛ Black (Incorrect letter)
- Prevents invalid, repeated or non-dictionary words
- Uses a customizable word list (`words.py`)
- Clean, interactive prompts

---

## 🛠 Requirements
- Python 3.7+
- `rich` Library

---

## 📦 Install Dependencies
```bash
pip install rich
```

---

## ▶️ How to Play
1. Clone or download the repository.
2. Make sure words.py contains a list named word_list of valid 5-letter words
3. Run the game - python game.py
4. Start guessing! After each guess, feedback is printed with colors and emoji.
