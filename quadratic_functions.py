# given a function ax^2 + bx + c = 0
def concavity(a, b, c):
    if a > 0:
        print("concave up")
    elif a < 0:
        print("concave down")
    else:
        print("no concavity")

def analyze(a , b, c):
    concavity(a, b, c)

analyze(5, 6, 6)


