"""
File: anagram.py
Name: GimmyLee 李庭侃
Time: 111/05/27 (五) ~ 111/06/03 (五)
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    1. Print the Welcome.
    2. Let user enter word, and remove the front and back space, to achieve case-insensitive.

    3. Judgment:
        3-1. If the input is equal to EXIT, end the program.
        3-2. If the input is word, continue to find the anagram.
    """
    print('Welcome to stanCode "Anagram Generator" (or', EXIT, 'to quit)')      # 1. Print the Welcome.

    while True:
        user_input_s = input('Type a word: ').strip().lower()                   # 2. User entered words.
        if user_input_s == EXIT:                                                # 3-1. End the program
            break
        else:
            find_anagrams(user_input_s)                                         # 3-2. Continue to find the anagram.


def read_dictionary(target_s):
    """
    :param target_s: string, user entered words.
    :return alphabet: list[string], find the existence of the word from the dictionary.
    -----------------------------------------------------------------------------
    This function mainly reads the file and reads English words from dictionary.txt.

    Basic Framework
        1. Read the file.
        2. Read the contents of the text file line by line.
        3. Remove the newline (\n) from the end of the sentence.
        4. Append the word to the list.
    Optimization
        Ⅰ. Judgment:
            If the word in the dictionary is of the same length as the word entered by the user,
            and by judging the letter of the word.
    """
    alphabet = []

    with open(FILE, 'r') as f:              # 1. Read the file.
        for word in f:                      # 2. Read the contents.
            word = word.strip()             # 3. Remove the newline (\n).
            if len(word) == len(target_s) and letter_check(word, target_s):     # Ⅰ. word length should be the same
                alphabet.append(word)  # 4. Append the word to the list.

    return alphabet


def letter_check(word, target_s):
    """
    :param word: string, find the word of the same length in the dictionary
    :param target_s: string, user entered words.
    :return: bool, Is the anagram of the word.
    -----------------------------------------------------------------------------
    Used to determine the number of letters in a word,
    if the number of letters in the dictionary is less than the one entered by the user,
    it means that the word will not be reorganized.

    e.g.
        word     == 'aardvark'
        target_s == 'contains'
        letter   == 'c'

    At this time, the target_s word contains the letter c, so the number is 1.
    the word doesn't have the letter c in it, so the number is 0,
    since there is no c in word, it cannot be a reorganization of target_s.
    """
    for letter in target_s:
        if word.count(letter) < target_s.count(letter):
            return False
    return True


def timer(func):
    """
    :param func: function, executed function.
    -----------------------------------------------------------------------------
    Written in decorator format,
    mainly used to test the execution time of find_anagrams().
    """
    def wrapper(s):
        start = time.time()
        func(s)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')
    return wrapper


@timer
def find_anagrams(s):
    """
    :param s: string, user entered words.
    ----------------------------------------------
    Check the words entered by the user to find out if there are any reorganized words.

    1. Read the dictionary: search the words entered by the user.
    2. Create list: after find_anagrams_helper process, the answer will be attached to this list, the purpose of creating here is to print the final result (number + regrouped words). 3.
    3. Call helper: the function that actually finds the function to reorganize the words.
    """
    dictionary_list = read_dictionary(s)                    # 1. Read the dictionary

    print('Searching...')
    ans_lst = []                                            # 2. Create list
    find_anagrams_helper(s, '', ans_lst, dictionary_list)   # 3. Call helper

    print(f'{len(ans_lst)} anagram: {ans_lst}')


def find_anagrams_helper(s, current_s, ans_lst, dictionary_list):
    """
    :param s: string, user entered words.
    :param current_s: string, used for concatenate prefix.
    :param ans_lst: string, record the anagram that match the answer.
    :param dictionary_list: list[str], list of words stored in the dictionary for optimizing recursion.
    -----------------------------------------------------------------------------
    The main purpose is to perform anagram word reorganization.

    Basic Framework
        1. Recursive Case
            1-1. choose     : Insert a letter at the end
            1-2. explore    : recursion.
            1-3. un-choose  : Remove a letter from the end.
        2. Base Case
            2-1. When the word "s" is given to all "current_s".
            2-2. and current_s is not in the answer before it is printed (to avoid duplicate answers).
    Optimization
        Ⅰ. If the first word is in the dictionary, then explore will continue.
    """
    if len(s) == 0:                                 # 2. Base Case
        if current_s not in ans_lst:                    # 2-2
            ans_lst.append(current_s)
            print('Found:', current_s)
            print('Searching...')

    else:                                           # 1. Recursive Case
        for i in range(len(s)):
            # 1-1. Choose
            current_s += s[i]
            unused_s = s[0:i]+s[i+1:]

            # 1-2. Explore
            if has_prefix(current_s, dictionary_list):          # Ⅰ. The first word is in the dictionary.
                find_anagrams_helper(unused_s, current_s, ans_lst, dictionary_list)

            # 1-3. Un-choose
            current_s = current_s[:-1]


def has_prefix(sub_s, dictionary_list):
    """
    The recursive case is performed only if the user enters a word whose initials are dictionary words.

    e.g.
        To find the word with c prefix, cat will return True and act will return False.
    """
    for word in dictionary_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
