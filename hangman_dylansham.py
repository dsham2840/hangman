# DOGMAN: Hangman without the Hanging
# Dylan Sham
#
#10/19/2016

import os
import random

def show_start_screen():
    print("_____________________________  ______________   __        ,                    ,\" e`--o")      
    print("___  __ \_  __ \_  ____/__   |/  /__    |__  | / /       ((                   (  | __,'")
    print("__  / / /  / / /  / __ __  /|_/ /__  /| |_   |/ /         \\~----------------' \_;/")
    print("_  /_/ // /_/ // /_/ / _  /  / / _  ___ |  /|  /          (                      /")           
    print("/_____/ \____/ \____/  /_/  /_/  /_/  |_/_/ |_/           /) ._______________.  )")
    print("         Press Enter to Start!                           (( (               (( ("    )
    print("                                                          ``-'               ``-'   ")
    input()

def show_credits():
    print("By the D-Man")
    print("           __            ___           ___           ___           ___           ___     ")
    print("          /\__\         /\  \         /\  \         /\__\         /\  \         /\__\    ")
    print("         /:/  /        /::\  \       /::\  \       /:/  /        /::\  \       /:/ _/_   ")
    print("        /:/__/        /:/\:\  \     /:/\:\  \     /:/__/        /:/\:\  \     /:/ /\__\  ")
    print("       /::\__\____   /::\~\:\  \   /:/  \:\  \   /::\  \ ___   /:/  \:\  \   /:/ /:/ _/_ ")
    print("      /:/\:::::\__\ /:/\:\ \:\__\ /:/__/ \:\__\ /:/\:\  /\__\ /:/__/ \:\__\ /:/_/:/ /\__\ ")
    print("      \/_|:|~~|~    \/__\:\/:/  / \:\  \  \/__/ \/__\:\/:/  / \:\  \ /:/  / \:\/:/ /:/  / ")
    print("         |:|  |          \::/  /   \:\  \            \::/  /   \:\  /:/  /   \::/_/:/  / ")
    print("         |:|  |          /:/  /     \:\  \           /:/  /     \:\/:/  /     \:\/:/  /  ")
    print("         |:|  |         /:/  /       \:\__\         /:/  /       \::/  /       \::/  /   ")
    print("          \|__|         \/__/         \/__/         \/__/         \/__/         \/__/    ")
    print("Created by Dylan Sham. Finalized on October 19, 2016.")
def get_category(path):
    files = os.listdir(path)

    print("Choose a category...")
    
    for i, f in enumerate(files):
        full_path = path + "/" + f

        with open(full_path, 'r') as file: 
            print(str(i+1) + ") " + file.readline().strip())

    choice = input("Enter selection: ")
    choice = (int(choice) - 1 )
    return path + "/" + files[choice]

def get_puzzle(file):
    #words = ["patriots", "jonathan pyle", "spicy memes", "jellyfish", "saucy", "rambunctious", "harambe didn't deserve to die", "juicy", "octopus", "pie", "oreo", "communism", "jaguar", "kenya", "allah akbar"]


    with open(file, 'r') as f:
        words = f.read().splitlines()

    return random.choice(words[1:]).lower()

def check(word, solved, guesses):
    for i in range(len(word)):
            if word[i] in guesses or not word[i].isalpha():
                solved = solved[:i] + word[i] + solved[i+1:]

    return solved

def get_guess():
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            return guess.lower()
        else:
            print("Please guess a single letter.")


def display_board(solved, guesses, strikes):

    if strikes == 0:
        print("")
    elif strikes == 1:
        print("                      ;\              ")
        print("                     |' \ ")
        print("  _                  ; : ; ")
        print(" / `-.              /: : | ")
      
    elif strikes == 2:
        print("                      ;\              ")
        print("                     |' \ ")
        print("  _                  ; : ; ")
        print(" / `-.              /: : | ")
        print(" |  ,-.`-.          ,': : | ")
        print("  \  :  `. `.       ,'-. : | ")
        print("   \ ;    ;  `-.__,'    `-.| ")
        print("  \ ;   ;  :::  ,::'`:.  `. ")
       
    elif strikes == 3:
        print("                      ;\              ")
        print("                     |' \ ")
        print("  _                  ; : ; ")
        print(" / `-.              /: : | ")
        print(" |  ,-.`-.          ,': : | ")
        print("  \  :  `. `.       ,'-. : | ")
        print("   \ ;    ;  `-.__,'    `-.| ")
        print("  \ ;   ;  :::  ,::'`:.  `. ")
        print("   \ `-. :  `    :.    `.  \ ")
        print("    \   \    ,   ;   ,:    (\ ")
        print("     \   :., :.    ,'o)): ` `-. ")
  
    elif strikes == 4:
        print("                      ;\              ")
        print("                     |' \ ")
        print("  _                  ; : ; ")
        print(" / `-.              /: : | ")
        print(" |  ,-.`-.          ,': : | ")
        print("  \  :  `. `.       ,'-. : | ")
        print("   \ ;    ;  `-.__,'    `-.| ")
        print("  \ ;   ;  :::  ,::'`:.  `. ")
        print("   \ `-. :  `    :.    `.  \ ")
        print("    \   \    ,   ;   ,:    (\ ")
        print("     \   :., :.    ,'o)): ` `-. ")
        print("    ,/,' ;' ,::\"'`.`---'   `.  `-._ ")
        print("  ,/  :  ; '\"      `;'          ,--`. ")
        print(" ;/   :; ;             ,:'     (   ,:) ")
      
    elif strikes == 5:
        print("                      ;\              ")
        print("                     |' \ ")
        print("  _                  ; : ; ")
        print(" / `-.              /: : | ")
        print(" |  ,-.`-.          ,': : | ")
        print("  \  :  `. `.       ,'-. : | ")
        print("   \ ;    ;  `-.__,'    `-.| ")
        print("  \ ;   ;  :::  ,::'`:.  `. ")
        print("   \ `-. :  `    :.    `.  \ ")
        print("    \   \    ,   ;   ,:    (\ ")
        print("     \   :., :.    ,'o)): ` `-. ")
        print("    ,/,' ;' ,::\"'`.`---'   `.  `-._ ")
        print("  ,/  :  ; '\"      `;'          ,--`. ")
        print(" ;/   :; ;             ,:'     (   ,:) ")
        print("   ,.,:.    ; ,:.,  ,-._ `.     \\""'/ ")
        print("   '::'     `:'`  ,'(  \`._____.-'\"' ")
        print("      ;,   ;  `.  `. `._`-.  \\ ")
        print("      ;:.  ;:       `-._`-.\  \`. ")
       
    elif strikes == 6:
        print("                      ;\              ")
        print("                     |' \ ")
        print("  _                  ; : ; ")
        print(" / `-.              /: : | ")
        print(" |  ,-.`-.          ,': : | ")
        print("  \  :  `. `.       ,'-. : | ")
        print("   \ ;    ;  `-.__,'    `-.| ")
        print("  \ ;   ;  :::  ,::'`:.  `. ")
        print("   \ `-. :  `    :.    `.  \ ")
        print("    \   \    ,   ;   ,:    (\ ")
        print("     \   :., :.    ,'o)): ` `-. ")
        print("    ,/,' ;' ,::\"'`.`---'   `.  `-._ ")
        print("  ,/  :  ; '\"      `;'          ,--`. ")
        print(" ;/   :; ;             ,:'     (   ,:) ")
        print("   ,.,:.    ; ,:.,  ,-._ `.     \\""'/ ")
        print("   '::'     `:'`  ,'(  \`._____.-'\"' ")
        print("      ;,   ;  `.  `. `._`-.  \\ ")
        print("      ;:.  ;:       `-._`-.\  \`. ")
        print("       '`:. :        |' `. `\  ) \ ")
        print("         ` ;:       |    `--\__,' ")
        print("            '`      ,' ")
        print("                 ,-' ")
        print("You just got Dogged!")
        


    print(solved + " [" + guesses + "]")

def play_again():

    while True:
        answer = input("Would you like to play again? ")

        if answer.lower() == 'no' or answer.lower() == "n":
            return False
        elif answer.lower() == 'yes' or answer.lower() == "y":
            return True

        print("Huh? Just say yes or no.")

def play():
    puzzle_dir = 'puzzles'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    solved = "-" * len(word)
    
    guesses = ""
    strikes = 0
    limit = 6
    
    solved = check(word, solved, guesses)
    display_board(solved, guesses, strikes)

    while word != solved and strikes < limit:
        letter = get_guess()

        if letter not in word:
            strikes += 1
            
        guesses += letter
        
        solved = check(word, solved, guesses)
        display_board(solved, guesses, strikes)

    if word == solved:
        print("You win!")
    else:
        print("You lose!")

def main():
    show_start_screen()

    playing = True

    while playing:
        play()
        playing = play_again()

    show_credits()


# code execution begins here
if __name__ == "__main__":
    main()
