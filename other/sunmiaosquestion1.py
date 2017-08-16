"""
A simple math quiz, based on the random questions by applying five
basic arithmetic operations and checking the results that user answered
is correct or not.
Author: Yiyin Sun
Username: ysun169
ID number: 554110799
"""
import random
def display_intro():
    title = "\n** A Simple Math Quiz **\n"
    frame = "*" * 24
    print(frame + title + frame)

def display_menu():
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Integer Division\n5. Modulo Operation\n6. Exit")

def display_separator():
    print("-" * 24)

def get_user_input():
    index = int(input("Enter your choice: "))
    while index != 1 and index != 2 and index != 3 and index != 4 and index != 5 and index != 6:
        print("Invalid menu option.\nPlease try again:")
        index = int(input("Enter your choice: "))
    return index

def get_user_solution(problem):
    print("Enter your answer")
    return user_solution

    
def check_solution(user_solution, solution, count):
    if user_solution == solution:
        print("Correct.")
        count += 1
        
    else:
        print("Incorrect.")
    return count
        
def menu_option(index, count):
    num1 = random.randrange(1,31)
    num2 = random.randrange(1,31)
    if index == 1:
        # user_solution = int(input(num1, "+", num2, "= "))
        user_solution = int(input('%d+%d= ' % (num1,num2)))
        solution = num1 + num2
    elif index == 2:
        user_solution = int(input(num1, "-", num2, "="))
        solution = num1 - num2
    elif index == 3:
        user_solution = int(input(num1, "*", num2, "="))
        solution = num1 * num2
    elif index == 4:
        user_solution = int(input(num1, "//", num2, "="))
        solution = num1 // num2
    elif index == 5:
        user_solution = int(input(num1, "%", num2, "="))
        solution = num1 % num2
    elif index == 6:
        print("Exit the quiz.")
    return count
    
def display_result(total, correct):
    percentage = correct / total * 100
    print("You answered " + str(total) + " questions with " + str(correct) + "correct.\n" + "Your score is " + str(percentage) + "%. Thank you.")
    return percentage

def main():
    display_intro()
    display_menu()
    display_separator()
    option = get_user_input()
    total = 0
    correct = 0
    while option != 6:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()
    
    print("Exit the quiz.")
    display_separator()
    display_result(total, correct)
    
main()
