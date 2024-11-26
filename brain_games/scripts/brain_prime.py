import random

def is_prime(n):
	if n <= 1:
		return false
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True

def main():
	print("Welcome to the Brain Games!")
	name = input("May I have your name? ")
	print(f"Hello, {name}!")

	questions = 3
	correct_a = 0

	while correct_a < questions:
		print('Answer "yes" if given number is prime. Otherwise answer "no".')
		number = random.randint(1, 100)
		correct_answer = "yes" if is_prime(number) else "no"
		print(f'Question: {number}')
		user_answer = input('Your answer: ')

		if user_answer.lower() != correct_answer:
			print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
			print(f"Let's try again, {name}!")
			return
		print("Correct!")
		correct_a += 1
	print(f"Congratulations, {name}!")

if __name__ == '__main__':
	main()
