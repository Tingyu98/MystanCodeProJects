"""
File: anagram.py
Name:Ting-Yu
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
    Input a word and find its anagrams
    """
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        s = input("Find anagrams for: ")
        if s == EXIT:
            break
        start = time.time()
        find_anagrams(s)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    """
    :param s: string, the word input by user
    :return lst: lst, a data container that stores the dictionary which will be looked up
    """
    lst = []
    with open(FILE, "r") as f:
        for word in f:
            word = word.strip()
            if len(word) == len(s):
                lst.append(word)
        return lst


def find_anagrams(s):
    """
    :param s: string, the word input by user
    """
    dic_lst = read_dictionary(s)
    lst = []
    print("Searching...")
    find_anagrams_helper(s, "", len(s), dic_lst, lst, [],)
    print(f"{len(lst)} anagrams: {lst}")


def find_anagrams_helper(s, current_s, ans_len, dict_lst, lst, index):
    """
    :param s: string, the word input by user
    :param current_s: string, used for concatenate prefix.
    :param ans_len: int, the length of the word input by user
    :param dict_lst: list[str], list of words stored in the dictionary for optimizing recursion.
    :param lst: list[str], record the anagram that match the answer
    :param index: list[str], record the index that its corresponding letters already used in current_s
    """
    if len(current_s) == ans_len:  # base cas
        if current_s in dict_lst:
            if current_s not in lst:
                print("Found: " + current_s)
                print("Searching...")
                lst.append(current_s)
    else:
        for i in range(ans_len):
            if len(current_s) == ans_len:
                break
            if i not in index:  # back-tracking
                # Choose
                if i not in index:
                    index.append(i)
                    current_s += s[i]
                # Explore
                    if has_prefix(current_s, dict_lst):  # early-stopping
                        find_anagrams_helper(s, current_s, ans_len, dict_lst, lst, index)
                # Un-choose
                    current_s = current_s[0:len(current_s)-1]
                    index.pop()


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: string, the prefix to search for
    :param dictionary: list[str], list of words stored in the dictionary for optimizing recursion.
    :return: boolean
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
