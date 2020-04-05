# Q1. Write a program that asks the user for a number if this number is even the program should print that it is even,
# otherwise it should print that it is odd.

# Create function to determine if a users numerical input is odd or even. String must be converted to a type int to be
# taken as an argument by the function


def odd_or_even():
    num = int(input("Enter a number: "))
    if num % 2 == 0:  # modulo of 2 will determine whether num is odd or even
        print(num, "is even!")  # to be printed if even
    else:
        print(num, "is odd!")  # to be printed if odd


odd_or_even()  # Call function
odd_or_even()  # Call function
odd_or_even()  # Call function
