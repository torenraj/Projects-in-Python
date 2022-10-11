import random as random

randNo = random.randint(1, 100)
# print(randNo)


userGuess = None
guesses = 0
while userGuess!=randNo:
    userGuess = int(input('Enter your guess: '))
    guesses+=1
    if(userGuess==randNo):
        print('You guessed it right!')
    else:
        if userGuess>randNo:
            print('You guessed it wrong! Enter a smaller number:')
        else:
            print('You guessed it wrong! Enter a greater number:')

print(f"You guessed the number in '{guesses}' guesses")

with open('/Users/torenraj/Desktop/python/highscore.txt') as f:
    content = int(f.read())


if guesses<content:
    print('Congratulations! you have just broke the record highscore')
    with open('/Users/torenraj/Desktop/python/highscore.txt', 'w') as f:
        f.write(str(guesses))
else:
    print('Better luck next time to break the record high score')



