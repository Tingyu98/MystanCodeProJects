"""
File: hangman.py
Name: Ting-YU
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program gives a random word and plays hangman game.
    """
    r_w = random_word()
    print(r_w)
    dashed_word = ""
    for i in range(len(r_w)):
        dashed_word += "-"
    print("The word looks like " + dashed_word)
    times = N_TURNS  # times == 能猜測的次數
    ans1 = dashed_word
    while True:
        if times > 0:
            print("You have " + str(times) + " wrong guesses left.")
            input_ch = input("Your guess: ")
            up_in_ch = input_ch.upper()  # up_in_ch == uppercase of input character
            if len(up_in_ch) == 1:
                if up_in_ch.isalpha():
                    guessing_process = ""
                    site = r_w.find(up_in_ch)  # site == 猜對的字母在 random word 中的 index
                    if site != -1:
                        print("You are correct!")
                        for i in range(len(r_w)):
                            if r_w[i] == up_in_ch:
                                guessing_process += up_in_ch
                            else:
                                guessing_process += "-"
                    else:
                        print("There is not " + up_in_ch + "'s in the word.")
                        times -= 1  # 猜錯字母，扣一次猜測機會
                        for i in range(len(r_w)):
                            guessing_process += "-"
                    ans2 = ""
                    for i in range(len(r_w)):
                        if ans1[i] == "-":
                            if guessing_process[i] == "-":
                                ans2 += "-"
                            else:
                                ans2 += guessing_process[i]
                        else:
                            ans2 += ans1[i]
                    ans1 = ans2
                    if ans1 != r_w:
                        if times > 0:
                            print("The word looks like " + ans1)
                else:
                    print("Illegal format.")
            else:
                print("Illegal format.")
            if ans1 == r_w:
                print("You win!!")
                break
        else:
            print("You are completely hung : (")
            break
    print("The word was: " + r_w)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
