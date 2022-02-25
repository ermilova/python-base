import random


def generate_test(mode):
    if mode == 1:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        operator = random.choice('+-*')
        print(a, operator, b)

        if operator == "+":
            return a + b
        elif operator == "*":
            return a * b
        elif operator == "-":
            return a - b
    else:
        a = random.randint(11, 29)
        print(a)
        return a ** 2


def test_user(mode, num=5):
    mark = 0
    for i in range(0, num):
        result = generate_test(mode)
        while True:
            try:
                user_answer = int(input())
                break
            except ValueError:
                print("Incorrect format.")

        if result == user_answer:
            print("Right!")
            mark += 1
        else:
            print("Wrong!")
    return mark


while True:
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    user_mode = input()
    if user_mode == "1" or user_mode == "2":
        break
    else:
        print("Incorrect format.")

if user_mode == "1":
    mark = test_user(1, 5)
else:
    mark = test_user(2, 5)

print("Your mark is " + str(mark) + "/5.")

file_saver = input("Would you like to save your result to the file? Enter yes or no.")
if file_saver in ["yes", "YES", "y", "Yes"]:
    user_name = input("What is your name?")
    result_file = open("results.txt", "a", encoding='utf-8')
    result_file.write(user_name + ": " + str(mark) + "/5 in level " + user_mode)
    if user_mode == "1":
        result_file.write("(simple operations with numbers 2-9).")
    else:
        result_file.write("(integral squares of 11-29).")
    result_file.close()
    print('The results are saved in "results.txt".')
