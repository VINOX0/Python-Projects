import random as rnd
import python_library as library
from rich import print
from rich.console import Console
from intro import banner
from intro import autor

# Einleitung
print(banner)
print(autor)
print("Willkommen zu Wordle!")
print("\n " * 2)

console = Console(force_terminal=True)
word = rnd.choice(library.woerter).upper()
word_length = len(word)
AMOUNT_OF_TRYS = 5
word_found = False
for y in range(AMOUNT_OF_TRYS):
    while True:
        guessed_word = input(f"Guess the word with {word_length} letters : ").upper()
        if len(guessed_word) == len(word):
            if guessed_word == word:
                print("You won!")
                word_found = True

            for i in range (len(guessed_word)):
                if guessed_word[i] == word[i]:
                    console.print(f"[black on bright_green]{guessed_word[i]}[/black on bright_green]",end="")
                elif guessed_word[i] in word:
                    console.print(f"[black on bright_yellow]{guessed_word[i]}[/black on bright_yellow]", end="")
                else:
                        console.print(f"[black on bright_red]{guessed_word[i]}[/black on bright_red]",end="")

            break
        else:
            print ("Word doesnt have the right amount of letters")
    if word_found:
        break
    print(f"You have {AMOUNT_OF_TRYS -y -1} trys left")
if not word_found:
    print(f"[black on bright_blue]{word}[/black on bright_blue]")














































