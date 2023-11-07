import math

# Input coefficients from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
