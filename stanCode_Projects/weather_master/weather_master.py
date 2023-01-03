"""
File: weather_master.py
Name:Betsy
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
	Find the highest temperature, lowest temperature, average temperature and the number of cold days in the data
	"""
	print("stanCode \"Weather Master 4.0\"!")
	data = int(input("Next Temperature: (or -100 to quit)? "))
	if data == EXIT:
		print("No temperatures were entered.")
	else:
		highest = data
		lowest = data
		a = 1
		s = data
		if data < 16:  # Whether the first data is a cold day
			low = 1
		else:
			low = 0
		while True:
			data = int(input("Next Temperature: (or -100 to quit)? "))
			if data == EXIT:
				break
			s = data + s  # The sum of data
			if data > highest:
				highest = data
			if data < lowest:
				lowest = data
			if data < 16:
				low += 1
			a += 1  # 計算有幾筆數值
		average = s / a
		print("Highest temperature= " + str(highest))
		print("Lowest temperature= " + str(lowest))
		print("Average = " + str(average))
		print(str(low) + " cold day(s)")




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
