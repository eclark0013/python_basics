# given a function y = ax^2 + bx + c
def analyze_quadratic(a, b, c):
    if a == 0:
        print("This is a linear function.")
    else:
        print(f"Given the function {a}x^2 + {b}x + {c} = 0 :")
        print(f"Concavity is {concavity(a, b, c)}.")
        print(f"Discriminant is {discriminant_value(a, b, c)}.")
        print(f"Number of roots: {roots_count(a, b, c)}.")
        print (f"Solutions are: {roots_of(a, b, c)}")

def concavity(a, b, c):
    if a > 0:
        return("up")
    else:
        return("down")

def discriminant_value(a, b, c): 
    return(b**2 - 4*a*c)

def roots_count(a, b, c):
    disc_value = discriminant_value(a, b, c)
    if disc_value > 0:
        return("two real roots")
    elif disc_value == 0:
        return("one real roots")
    else: 
        return("two imaginary roots")

def roots_of(a, b, c):
    disc_value = discriminant_value(a, b, c)
    if disc_value > 0:
        return([((-b+disc_value)/(2*a)), (-b-disc_value)/(2*a)])

analyze_quadratic(1, 5, 6)
""" To do next:
- complete solutions for other values
- show intervals where function is positive or negative
- find tangent line to function at a given x value"""



