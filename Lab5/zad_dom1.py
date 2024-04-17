import math

def f(x):
    return 1/(1+x*x)

def squares(f, start = 0, end = 1, h=0.001):
    res = 0
    x = start
    while x < end:
        res += f(x)*h 
        x+=h
    return res


if __name__ == "__main__":
    accuracy = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    print("Solutions:")
    print("acc      squares       squares_diff ")
    for acc in accuracy:
        squares_result = squares(f, 0, 1, acc)
        squares_difference = abs(squares_result - math.pi/4)
        
        print(f"{acc:<8.4f} {squares_result:<14.8f} {squares_difference:<14.8f}  ")
