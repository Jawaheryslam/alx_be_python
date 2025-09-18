first_number = int(input("Enter the first number: "))
second_number = int(input("enter the second number: "))
operation = input("Choose the operation (+, -,*, /): ")

match operation:
    case "+":
        print(f"The result is {first_number + second_number}.")
    case "-":
        print(f"The result is {first_number - second_number}.")
    case "*":
        print(f"The result is {first_number * second_number}.")
    case"/":
        if first_number == 0 or second_number == 0:
            print("Cannot divide by zero")
        else:
            print(f"The result is {first_number / second_number}.")
