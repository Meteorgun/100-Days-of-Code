from art import logo

#Add


def add(num1, num2):
    return num1 + num2

#Substraction


def sub(num1, num2):
    return num1 - num2

#Multiplication


def multiply(num1, num2):
    return num1 * num2

#Division


def div(num1, num2):
    return num1 / num2


operations = {"+": add,
              "-": sub,
              "*": multiply,
              "/": div
              }


def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    while True:
        for i in operations:
            print(i)
        question = input("What operation do you want do? ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[question]
        answer = calculation_function(num1, num2)
        print(f"{num1} {question} {num2} = {answer}")
        num1 = answer
        confirm = input(
            "Type 'y' to continue calculating with  or type 'n' to exit. : ").lower()
        if confirm == "n":
            break


calculator()
