# given a function ax^2 + bx + c = 0
def analyze(a, b, c):
    print(f"Concavity is {concavity(a, b, c)}")
    print(f"Discriminant is {discriminant_value(a, b, c)}")
    print(f"Number of roots: {roots_count(a, b, c)}")

def concavity(a, b, c):
    if a > 0:
        return("up")
    elif a < 0:
        return("down")
    else:
        return("none")

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

analyze(5, 6, 6)




