# given a function f(x) = ax^2 + bx + c
import math

def analyze_quadratic(a, b, c):
    if a == 0:
        print("This is a not a quadratic function.")
    else:
        print(f"Given the function f(x) = {a}x^2 + {b}x + {c} :")
        print(f"Concavity: {concavity(a, b, c)}")
        print(f"Discriminant: {discriminant_value(a, b, c)}")
        print(f"Number of roots: {roots_count(a, b, c)}")
        print (f"Root(s): {" and ".join(map(str, (roots_of(a, b, c))))}")
        print (f"Extremum found at {extremum_x(a, b, c), function_value(a, b, c, extremum_x(a, b, c))}")

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
        return("one real root")
    else: 
        return("two imaginary roots")

def roots_of(a, b, c):
    disc_value = discriminant_value(a, b, c)
    if disc_value > 0:
        return([(-b+math.sqrt(disc_value))/(2*a), (-b-math.sqrt(disc_value))/(2*a)])
    elif disc_value == 0:
        return [((-b)/(2*a))]
    else:
        return([f"({-b}+{math.sqrt(-disc_value)}i)/{2*a}", f"({-b}-{math.sqrt(-disc_value)}i)/{2*a}"])
    
def function_value(a, b, c, x):
    return (a*x**2 + b*x + c)

def extremum_x(a, b, c):
    return (-b/(2*a))

analyze_quadratic(1, 4, 3)

""" To do next:
- show intervals where function is positive or negative
- find tangent line to function at a given x value"""



