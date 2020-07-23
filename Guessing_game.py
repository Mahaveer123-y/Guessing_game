secret_number = 18
no_of_guesses = 1
print("You have only 9 guesses")
while (no_of_guesses <=9):
    guess_number = int(input("Please Guess the number\n"))
    if guess_number <18:
        print("You enter less no please enter high no\n")
    elif (guess_number > 18):
        print(("You entered high no please enter low no\n"))

    else:
        print("you win\n")
        print(no_of_guesses ,"no of guesses took to finish")
        break
    print(9-no_of_guesses,"no of guesses left")
    no_of_guesses = no_of_guesses +1
if(no_of_guesses >9):
    print("game over")



