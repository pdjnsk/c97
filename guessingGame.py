import random

number = random.randint(1,9)
print(number)
print("guess number between 1 to 9")
guess = int(input("guess the number: "))

chances = 0


while chances == 0:

    if guess == number:
        print("YOU WON")
        chances=chances+1
        break

    if (guess < number):
        print("your guess is too low. Enter number more than ",guess)
        chances=chances+1
        break

    if (guess > number):
        print("your guess is too high. Enter number less than ",guess)
        chances=chances+1
        break

if guess != number:

    guess2 = int(input("guess the number: "))

    while chances == 1:

        if guess2 == number:
            print("YOU WON")
            chances=chances+1
            break

        if (guess2 < number):
            print("your guess is too low. Enter number more than ",guess2)
            chances=chances+1
            break

        if (guess2 > number):
            print("your guess is too high. Enter number less than ",guess2)
            chances=chances+1
            break
    if guess2 != number:

        guess3 = int(input("guess the number: "))

        while chances == 2:

          if guess3 == number:
            print("YOU WON")
            chances=chances+1
            break

          if (guess3 < number):
            print("your guess is too low. Enter number more than ",guess3)
            chances=chances+1
            break

          if (guess3 > number):
            print("your guess is too high. Enter number less than ",guess3)
            chances=chances+1
            break

        if guess3 != number:

            guess4 = int(input("guess the number: "))

            while chances == 3:

                if guess4 == number:
                  print("YOU WON")
                  chances=chances+1
                  break

                if (guess4 < number):
                   print("your guess is too low. Enter number more than ",guess4)
                   chances=chances+1
                   break

                if (guess4 > number):
                   print("your guess is too high. Enter number less than ",guess4)
                   chances=chances+1
                   break

            if guess4 != number:

                guess5 = int(input("guess the number: "))

                while chances == 4:

                    if guess5 == number:
                        print("YOU WON")
                        
                        break

                    if (guess5 < number):
                        print("your guess is too low. Enter number more than ",guess5)
                        
                        break

                    if (guess5 > number):
                        print("your guess is too high. Enter number less than ",guess5)
                        
                        break

    

if  chances == 5 :
    print("YOU LOSE the number is: ",number)