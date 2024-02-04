import random
import check_input
from dictionary import words


def display_gallows(num_incorrect):
    #display the state of the hangman on the gallows
    print("========")
    print("||/   |")
    if num_incorrect == 0:
        print("||")
        print("||")
        print("||")
    if num_incorrect == 1:
        print("||    o")
        print("||")
        print("||")
    if num_incorrect == 2:
        print("||    o")
        print("||    |")
        print("||")
    if num_incorrect == 3:
        print("||    o")
        print("||    |")
        print("||   /")
    if num_incorrect == 4:
        print("||    o")
        print("||    |")
        print("||   / \\")
    if num_incorrect == 5:
        print("||   \\o")
        print("||    |")
        print("||   / \\")
    if num_incorrect == 6:
        print("||   \\o/")
        print("||    |")
        print("||   / \\")

    print("||\n")


def display_letters(letters):
    #display each of the letters separated by spaces.
    for l in letters:
        print(l + " ", end="")
    print("\n")

def get_letter_remaining(incorrect, correct): 
    # return list of remaining letters in the alphabet to choose from 
    # remove both correct and incorrect from the remaining
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    for l in incorrect:
        if l in alpha:
            alpha.remove(l)

    for l in correct:
        if l in alpha:
            alpha.remove(l)

    return alpha


def main():
    print("-Hangman-\n")
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    play = True

    while play:
        #initilize game with random word
        answer = random.choice(words)

        #print answer
        incorrect = []
        correct = ["_", "_", "_", "_", "_"]
        incorrect_count = 0
        correct_count = 0



        #continue the game until user wins or loses
        while incorrect_count !=6 and correct_count != 5:
            incorrect.sort()
            print("Incorrect selections: ", end ="")
            display_letters(incorrect)
            display_gallows(incorrect_count)
            display_letters(correct)
            print("Letter remaining: ", end="")
            display_letters(get_letter_remaining(incorrect, correct))

            #get user's guess

            letter = input("Enter a letter: ").upper()
            if letter in correct or letter in incorrect:
                print("You have aldready used that letter.")
            elif letter not in alpha:
                print("That is not a letter.")
            else:
                #check if guess is correct
                if letter in answer:
                    print("Correct!\n")
                    # add correct letter at right location
                    for l in range(len(answer)):
                        if answer[l] == letter:
                            correct[l] = letter
                            correct_count += 1
                else:
                            #add letter to incorrect list
                    print("Incorrect!\n")
                    incorrect_count += 1
                    incorrect.append(letter)
        #display final result
        display_gallows(incorrect_count)
        display_letters(correct)
        if incorrect_count == 6:
            print("You died!")
            print("The correct answer was: " + answer)
        else:
            print("You win!")

        play = check_input.get_yes_no("Play again (Y/N)?")

main()


