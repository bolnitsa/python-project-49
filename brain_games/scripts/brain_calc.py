import random

def random_expression():

    operations = ['+', '-', '*']
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operation = random.choice(operations)
    return num1, operation, num2

def result(num1, operation, num2):

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2

def main():

    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    questions = 3
    correct_a = 0

    while correct_a < questions:
        num1, operation, num2 = random_expression()
        print("What is the result of the expression?")
        print(f"Question: {num1} {operation} {num2}")

        answer = input("Your answer: ")



        answer = int(answer)
        correct_answer = result(num1, operation, num2)

        if answer != correct_answer:
            print(f"{answer} is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
        correct_a += 1
    print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()
