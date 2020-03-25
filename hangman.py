from string import ascii_lowercase
import random
import sys


def play():
    x = 0
    while x == 0:
        toplay = input('\nType "play" to play the game, "exit" to quit: ')
        if toplay == 'play':
            x += 1
            continue
        if toplay == 'exit':
            sys.exit()
        else:
            continue


play()
print('\nH A N G M A N')

langs = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(langs)
state = "-" * len(word)
message = 'Input a letter: '
wrong_message = 'No such letter in the word'
incorrect = 8
stop = 0
guessed = []

while incorrect != 0 and stop == 0:
    print("\n" + "".join(state))
    guess = input(message)
    if incorrect == 0:
        print(wrong_message)
        print('You are hanged!')
        break
    if len(guess) != 1:
        print("You should print a single letter")
    elif guess not in ascii_lowercase:
        print("It is not an ASCII lowercase letter")
    elif len(guess) == 1 and guess.isalpha():
        if guess in guessed:
            print('You already typed this letter')
        elif guess in state and guess not in guessed:
            print('You already typed this letter')
        elif guess in word:
            for index, character in enumerate(word):
                state = list(state)
                if character == guess:
                    state[index] = guess
                    current = "".join(state)
                    guessed.append(current)
                    if current == word:
                        print('You survived!')
                        stop += 1
                        play()
        elif guess in ascii_lowercase and guess not in word and guess not in guessed:
            if incorrect == 1:
                print(wrong_message + '\nYou are hanged!')
                stop += 1
                play()
                break
            else:
                print(wrong_message)
                guessed.append(guess)
                incorrect -= 1
