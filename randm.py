import random
randnumber = random.randint(1,100)

userGuess = None
guesses = 0

while (userGuess != randnumber):
    userGuess = int(input('Enter your guess : '))
    guesses +=1
    if userGuess == randnumber:
        print('You guessed it right!!')
    else:
        if userGuess > randnumber:
            print('You guessed it wrong Enter a Smaller number!!')
        else:
            print('You guessed it wrong Enter a Larger number!!')

print(f'You have gussed it in {guesses} guesses')

with open('highscore.txt','r')as f:
    highscore = int(f.read())

if (guesses< highscore):
    print('you have just broken the highscore!!!')
    with open('highscore.txt','w')as f:
        f.write(str(guesses))

