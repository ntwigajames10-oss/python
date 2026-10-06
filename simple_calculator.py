#instructions = ("choose two numbers from 0 to 9, x represents the first number while y represent the second")
#print("Note: you can exit the program at any point by simply typing "quit")
#WHILE True
    #input(x)
    #input(y)
    #IF x and y are not integers THEN
        #print("sorry please insert valid numbers")
    #ELSE IF
    #ELSE
        #print('''
                #choose the desired operation
                #(A) --> addition
                #(S) --> subtraction
                #(M) --> multiplication
                #(D) --> division
                #''')
    #input(choice)
    #IF choice == "A" THEN
        #answer = (x + y)
    #ELSE IF choice == "S" THEN
        #answer = (x - y)
    #ELSE IF choice == "M" THEN
        #answer = (x * y)
    #ELSE IF choice == "D" THEN
        #answer = (x / y)
    #ELSE
        #print("please choose a valid choice ")

def addition_function():
    sum = num1 + num2
    return sum

def subtraction_function():
    difference = num1 - num2
    return difference

def multiplication_function():
    multiplication = num1 * num2
    return multiplication

def division_function():
    division = num1 / num2
    return division

print("""
choose two numbers from 0 to 9, x represents the first number while y represent the second
Note: you can exit the program at any point by simply typing "quit
""")
while True:
    num1 = int(input("Enter first number(num1): "))
    num2 = int(input("Enter second number(num2): "))

    print("""
    choose the operation:
    A --> addition
    S --> subtraction
    M --> multiplication
    D --> division
    """)
    operation = input("Enter operation: ")
    if operation == "A" or operation == "a":
        print(addition_function())

    elif operation == "S":
        print(subtraction_function())

    elif operation == "M":
        print(multiplication_function())

    elif operation == "D":
        print(division_function())

    elif operation == "Q" or operation == "q" or operation == "quit" or operation == "Quit":
        break

    else:
        print("Invalid operation")