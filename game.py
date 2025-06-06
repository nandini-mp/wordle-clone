from rich.console import Console
from rich.prompt import Prompt
from random import choice
from words import word_list
from collections import Counter

welcomeMessage = f'\n[white on blue] Welcome to Wordle [/]\n'
playerInstructions = "You may start guessing\n"
guessStatement = "\nEnter your guess"
allowedGuesses = 6

squares = {'correct_place': '🟩','correct_letter': '🟨','incorrect_letter': '⬛'}

def correct_place(letter):
    return f'[black on green]{letter}[/]'

def correct_letter(letter):
    return f'[black on yellow]{letter}[/]' 

def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'

def check_guess(guess, answer):
    guessed = []
    wordle_pattern = []
    result = [''] * 5
    answer_counts = Counter(answer)
    
    # First pass: Correct letters in correct place
    for i in range(5):
        if guess[i] == answer[i]:
            result[i] = 'correct_place'
            answer_counts[guess[i]] -= 1

    # Second pass: Correct letters in wrong place
    for i in range(5):
        if result[i] == '':
            if guess[i] in answer_counts and answer_counts[guess[i]] > 0:
                result[i] = 'correct_letter'
                answer_counts[guess[i]] -= 1
            else:
                result[i] = 'incorrect_letter'

    # Build the display
    for i, res in enumerate(result):
        if res == 'correct_place':
            guessed.append(correct_place(guess[i]))
            wordle_pattern.append(squares['correct_place'])
        elif res == 'correct_letter':
            guessed.append(correct_letter(guess[i]))
            wordle_pattern.append(squares['correct_letter'])
        else:
            guessed.append(incorrect_letter(guess[i]))
            wordle_pattern.append(squares['incorrect_letter'])

    return ''.join(guessed), ''.join(wordle_pattern)

def game(console,chosen_word):
    endOfGame = False
    alreadyGuessed = []
    fullWordlePattern = []
    allWordsGuessed = []
    while not endOfGame:
        guess = Prompt.ask(guessStatement).upper()
        while len(guess)!=5 or guess in alreadyGuessed or guess not in word_list:
            if guess in alreadyGuessed:
                console.print("[red]You've already guessed this word!\n[/]")
            elif guess not in word_list:
                console.print("[red]Not a valid word. Try again!\n[/]")
            else:
                console.print("[red]Please enter a 5-letter word!\n[/]")
            guess=Prompt.ask(guessStatement)
        alreadyGuessed.append(guess)
        guessed, pattern = check_guess(guess,chosen_word)
        allWordsGuessed.append(guessed)
        fullWordlePattern.append(pattern)
        console.print(*allWordsGuessed,sep="\n")
        if guess==chosen_word or len(alreadyGuessed)==allowedGuesses:
            endOfGame = True
    if len(alreadyGuessed)==allowedGuesses and guess!=chosen_word:
        console.print(f"\n[red]WORDLE X/{allowedGuesses}[/]")
        console.print(f'\n[green]Correct Word: {chosen_word}[/]')
    else:
        console.print(f"\n[green]WORDLE {len(alreadyGuessed)}/{allowedGuesses}[/]\n")
    console.print(*fullWordlePattern,sep="\n")

if __name__ == '__main__':
    console = Console()
    chosen_word=choice(word_list)
    console.print(welcomeMessage)
    console.print(playerInstructions)
    game(console,chosen_word)
