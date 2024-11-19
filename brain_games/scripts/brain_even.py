import random

def is_even(number):
    return number % 2 == 0

def get_correct_answer(number):
    return 'yes' if is_even(number) else 'no'

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    questions_to_answer = 3
    correct_answers = 0

    while correct_answers < questions_to_answer:
        number = random.randint(1, 100)
        correct_answer = get_correct_answer(number)

        print(f"Question: {number}")
        user_answer = input('Your answer: ').strip().lower()

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("Correct!")
        correct_answers += 1

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
