import random

print("----------------------------------------------------------------------------------------------------")
print("|THIS IS A GUESSING GAME :items to guess are as follows which do you think is correct guess!!!      |")
print("----------------------------------------------------------------------------------------------------")
print("|1.strawberry                                                                                       |")
print("----------------------------------------------------------------------------------------------------")
print("|2.mango                                                                                            |")
print("----------------------------------------------------------------------------------------------------")
print("|3.apple                                                                                            |")
print("----------------------------------------------------------------------------------------------------")
print("|4.grape                                                                                            |")
print("----------------------------------------------------------------------------------------------------")
print("|5.banana                                                                                           |")
print("----------------------------------------------------------------------------------------------------")



while True:
    list_1 =["strawberry","mango","apple","grape","banana"]
    computer_choice = random.choice(list_1)
    user_choice = input("Enter your guess from the list as displayed (in lowercase):")

    if computer_choice == user_choice:
        print("YAY!,you guessed correct")
        print("CODE LEVEL 3:bombshell")
        z = input("ENTER CODE :")
        if z == "bombshell":
                exit()
        else:
            print("Try again")
            z = input("ENTER CODE :")
                
    
    else:
        print("Wrong guess try again")

    play_again = input("do you want to play again type y/n (lowercase) :")
    if play_again != "y":
        break
