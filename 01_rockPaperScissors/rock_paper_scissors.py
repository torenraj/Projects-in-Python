import random

def gamewin(com, you):
    if com == you:
        return None
    elif com == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif com == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif com == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True


print("Comp Turn: Rock(r) Paper(p) or Scissors(s)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    com = 'r'
elif randNo == 2:
    com = 'p'
elif randNo == 3:
    com = 's'

you = input("Your Turn: Rock(r) Paper(p) or Scissors(s)?")
a = gamewin(com, you)

print('computer choose: ', com)
print('You choose: ', you)



if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
