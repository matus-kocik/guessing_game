""" 
Jeste jeden ukol
Zeptejte se hrace jak se jmenuje
Vypiste mu neco jako print(f"Vyborne, hraci {player_name}. Myslim si cislo od 1 do 20")
Vygenerujte si random cislo
Ve trech pokusech muze zkusit cislo uhodnout, pokud cislo neuhodne a ma jeste zbyvajici pokusy, tak vypiste jestli myslene cislo je vetsi nebo mensi
Pokud uhodne cislo tak vypiste hraci neco jako super hraci_1 vyhral si, myslene cislo je x
v opacnem pripade nevadi, muzes to zkusit znovu, myslene cislo je x
Bonus: Na konci se zeptejte jestli se chce hrac hrat znovu, pokud ano tak spustte hry znovu s nove vygenerovanym cislem
"""

import random
import time


def guess_game():
    player_name = input("Welcome to the guessing game. What is your name?\n")
    
    # print(f"Hello {name}, this is guessing game.")
    # time.sleep(2)
    # print(f"I think a number between 1-20.")
    # time.sleep(2)
    # print("You've got only 3 tips, but I help you :).")
    # time.sleep(2)
    # print("Please, guess the number!")
    
    message = [
               f"Hello {player_name}, this is guessing game.",
               f"I think a number between 1-20.",
               f"You've got only 3 tips, but I help you :)."
               f"Please, guess the number!"
               ]
    
    for msg in message:
        print(msg)
        time.sleep(2)

    
    think_number = random.randint(1,20)
    guess_tip = 3

    while guess_tip > 0:
        try:
            guess = int(input("What number I think?: \n"))
            
            if guess == think_number:
                print(f"You win! I think {think_number}")
                break             
            else:
                guess_tip -= 1
                if guess_tip != 0:
                    if guess > think_number:
                        print("Wrong. You need to guess lower.")
                    else:           
                        print("Wrong. You need to guess higher.")
                else:        
                    print(f"You lose! The number was {think_number}.")
                    break
        except ValueError:
            print(f"Please enter a number between 1 and 20.")
            
    while True:        
        play_again = input("Do you want play again? (Y/N)\n")
        if play_again.lower() == "y":
            guess_game()
            break
        else:
            print(f"Thank you {player_name}, Bye!")
            break

    
guess_game() 
