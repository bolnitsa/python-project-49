import random
import math

def random_num():
	num1 = random.randint(1,100)
	num2 = random.randint(1,100)
	return num1, num2

def correct(num1, num2):
	return math.gcd(num1, num2)

def main():
	print("Welcome to the Brain Games!")
	name = input("May I have your name? ")
	print(f"Hello, {name}!")

	questions = 3
	correct_a = 0

	while correct_a < questions:
		num1, num2 = random_num()
		print("Find the greatest common divisor of given numbers.")
		print(f"Question: {num1} {num2}")

		answer = input("Your anwser: ")
		correct_answer = correct(num1, num2)
		answer = int(answer)
		if answer != correct_answer:
			print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
			print(f"Let's try again, {name}!")
			return
		print("Correct!")
		correct_a += 1
	print(f"Congratulations, {name}!")

if __name__ == '__main__':
	main()
