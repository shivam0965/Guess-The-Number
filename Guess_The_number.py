import random

print('----------------------------')
print('      GUESS THE NUMBER      ')
print('----------------------------')

randomNumber = random.randint(15, 30)
totalGuess = 0

while True:
    userInput = int(input('Enter a Number between 15 to 30: '))
    totalGuess += 1

    if userInput > 30 or userInput < 15:
        print('Invalid Input')
        print()
        totalGuess -= 1
        continue

    elif userInput == randomNumber:
        print('Congrats!! You Guessed it RIGHT.')
        print("Your Score: ", totalGuess)
        print()
        
        option = 0;

        while True:
            print('----------------------------')
            print()
            print('01. Play Again')
            print('02. Exit')
            print()

            option = int(input('Enter Option: '))

            if option == 1 or option == 2:
                break
            else:
                print('Invalid Input')
                print()
                continue
                
        if option == 1:
            randomNumber = random.randint(15, 30)
            totalGuess = 0
            print()
            continue
        elif option == 2:
            print()
            print('----------------------------')
            break


    elif userInput > randomNumber:
        print('Too High')
        print()
        continue

    else:
        print('Too Low')
        print()
        continue