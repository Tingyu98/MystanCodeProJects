"""
File: largest_digit.py
Name: GimmyLee 李庭侃
Time: 111/05/25 (三)
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the number entered by the user.
	:return: recursion, compare the largest number in the number position.
	--------------------------------
	Thinking:
		1. Two numeric variables are needed to compare the size of the two.
		2. The last position of the number is given priority,
			so the concept of "remainder" is used to take out the last position.

	Step:
		1.  If the value of n passed in is negative, first convert it to a positive value.
	"""
	if n < 0:		# 1. Negative to positive.
		n *= -1

	return find_largest_digit_helper(n, -float("inf"))


def find_largest_digit_helper(n, bigger):
	"""
	:param n: int, the number entered by the user.
	:param bigger: int, compare the largest number in the number position.
	:return bigger: int, compare the largest number in the number position.
	------------------------------------------------
	1. Recursive Case：
		1-1. Determine if the value is larger than the original value by comparing the position of the digits.
		1-2. Replace it if it's bigger.
		1-3. remove the last digit by n//10 during recursion
				because the last position of the value has been compared by mod.

	2. Base Case:
			In "Recursive Case", the number of digits is removed by n//10,
			so the length of the value will become less and less,
			when only a single-digit value remains, it will happen that n//10 == 0,
			as a result, just send back the bigger number.
	"""
	if n == 0:					# 2. Base Case
		return bigger

	else:						# 1. Recursive Case
		mod = n % 10
		if mod > bigger:		# 1-1. If the last position of the input number is larger than the original.
			bigger = mod		# 1-2. Replace it.

		# 1-3. Because the last position of the value has been compared by mod,
		# so remove the last digit by n//10 during recursion
		return find_largest_digit_helper(n//10, bigger)


if __name__ == '__main__':
	main()
