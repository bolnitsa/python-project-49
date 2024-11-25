import random

def generate_progression(lenght, start, step):
	return [start + step * i for i in range(lenght)]

def hide_number(progression):
	index = random.randint(0, len(progression) - 1)
	number = progression[index]
	progression[index] = '..'
	return number, index, progression

def main():
	print("Welcome to the Brain Games!")
	name = input(f"May I have your name? ") 
	print(f"Hello, {name}!")

	questions = 3
	correct_a = 0

	while correct_a < questions:
		progression_lenght = random.randint(5,10)
		start = random.randint(1, 10)
		step = random.randint(1,5)
		progression = generate_progression(progression_lenght, start, step)
		number, index, displayed_progression = hide_number(progression)
		print("What number is missing in the progression?")
		print("Question:", ' '.join (str(x) for x in displayed_progression))
		user_answer = input("Your answer: ")

		user_answer = int(user_answer)

		if user_answer != number:
			print(f"{user_answer} is wrong answer ;(. Correct answer was '{number}'.")
			print(f"Let's try again, {name}!")
			return
		print("Correct!")
		correct_a += 1
	print(f"Congratulations, {name}!")

if __name__ == '__main__':
	main()
