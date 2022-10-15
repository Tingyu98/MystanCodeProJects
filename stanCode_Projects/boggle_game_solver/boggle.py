"""
File: boggle.py
Name: Ting-Yu
----------------------------------------
Chain the connected letters to find all the existing words.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	input four rows of letters, and chain the connected letters to find all the existing words
	"""
	####################
	row1 = input("1 row of letters: ")
	row2 = input("2 row of letters: ")
	row3 = input("3 row of letters: ")
	row4 = input("4 row of letters: ")
	start = time.time()
	find_anagrams(row1, row2, row3, row4)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	:return: dict_, dict,include words containing more than four letters, arranged alphabetically
	"""
	dict_ = {}
	with open(FILE, "r") as f:
		for word in f:
			word = word.strip()
			if len(word) >= 4:
				if word[0] not in dict_:
					dict_[word[0]] = [word]
				else:
					dict_[word[0]].append(word)
		return dict_


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary: dict, include words containing more than four letters, arranged alphabetically
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	if sub_s[0] in dictionary:
		lst = dictionary[sub_s[0]]
		for word in lst:
			if word.startswith(sub_s):
				return True
	return False


def find_anagrams(row1, row2, row3, row4):
	dict_ = read_dictionary()
	row1_str = ""
	row2_str = ""
	row3_str = ""
	row4_str = ""
	ch_lst = []
	for i in range(0, 7, 2):
		row1_str += row1[i].lower()
	for i in range(0, 7, 2):
		row2_str += row2[i].lower()
	for i in range(0, 7, 2):
		row3_str += row3[i].lower()
	for i in range(0, 7, 2):
		row4_str += row4[i].lower()
	ch_lst.append(row1_str)
	ch_lst.append(row2_str)
	ch_lst.append(row3_str)
	ch_lst.append(row4_str)

	counter = [0]
	anagrams_lst = []
	for i in range(4):
		for j in range(4):
			current_s = ch_lst[i][j]
			x = i
			y = j
			find_anagrams_helper(ch_lst, current_s, x, y, dict_, counter, anagrams_lst, [(i, j)])
	print(f"There are {counter} words in total.")


def find_anagrams_helper(ch_lst, current_s, x, y, dict_, counter, anagrams_lst, index):
	"""
	:param ch_lst: lst, Include four lines of typed letters
	:param current_s: string, current string
	:param x: int, index of current string
	:param y: int, index of current string
	:param dict_: dict, including words containing more than four letters, arranged alphabetically
	:param counter: int, numbers of found words
	:param anagrams_lst: lst, including found words
	:param index: lst, including index of found words
	"""
	if len(current_s) >= 4:  # Base case
		if current_s in dict_[current_s[0]]:
			if current_s not in anagrams_lst:
				print(f"Found: {current_s}")
				counter[0] += 1
				anagrams_lst.append(current_s)
	for i in range(-1, 2):
		for j in range(-1, 2):
			if 3 >= (y + j) >= 0 and 3 >= (x + i) >= 0:
				if ((x + i), (y + j)) not in index:  # Back-tracking
				# Choose
					index.append(((x + i), (y + j)))
					current_s += ch_lst[x+i][y+j]
				# Explore
					if has_prefix(current_s, dict_):  # Early-stopping
						find_anagrams_helper(ch_lst, current_s, x+i, y+j, dict_, counter, anagrams_lst, index)
				# Un-choose
					current_s = current_s[0:len(current_s)-1]
					index.pop()


if __name__ == '__main__':
	main()
