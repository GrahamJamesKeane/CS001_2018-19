# Graham Keane 18146619 CS001
# Question 5

# Writing a Python program that calculates the area, and the circumference, of a circle

# Variables r and p (pi) defined by user input
r = input("Enter a radius value please: ")
p = 3.14159

# Formula for Area and Circumference
AREA = p * (float(r) ** 2)
CIRCUMFERENCE = 2 * p * float(r)

print("The area of your circle is " + str(AREA) + str(" M."))

print("The circumference of your circle is " + str(CIRCUMFERENCE) + str(" M."))
