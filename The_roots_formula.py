import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

D = b*b - 4*a*c
answer_1 = (-1*b - math.sqrt(D)) / (2 * a)
answer_2 = (-1*b + math.sqrt(D)) / (2 * a)

print (f"x1 = {answer_1}")
print (f"x2 = {answer_2}")
