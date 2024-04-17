import math

def f(x):
    return 1/(1+x)

def squares(f, start = 0, end = 1, n = 10):
    res = 0
    x = start
    h = (end-start)/n
    while x < end:
        res += f(x)*h 
        x+=h
    return res

def trapezoidal(f, start = 0, end = 1, n = 10):
    res = 0
    x = start
    h = (end-start)/n
    while x + h <= end:
        res += (f(x)+f(x+h))*h/2 
        x+=h
    return res

def simpson(f, start = 0, end = 1, n = 10):
    res = 0
    x = start
    h = (end-start)/n
    while x + h <= end:
        res += (f(x)+4*f((2*x+h)/2)+f(x+h))*h/6 
        x+=h
    return res

if __name__ == "__main__":
    accuracy = [1, 3, 5, 10, 100]
    print("Solutions:")
    print("n      squares        trapezoidal    simpson        squares_diff    trapezoidal_diff  simpson_diff")
    for acc in accuracy:
        squares_result = squares(f, 0, 1, acc)
        trapezoidal_result = trapezoidal(f, 0, 1, acc)
        simpson_result = simpson(f, 0, 1, acc)
        squares_difference = abs(squares_result - math.log(2))
        trapezoidal_difference = abs(trapezoidal_result - math.log(2))
        simpson_difference = abs(simpson_result - math.log(2))

        
        print(f"{acc:<8.4f} {squares_result:<14.8f} {trapezoidal_result:<14.8f} {simpson_result:<14.8f} {squares_difference:<14.8f}  {trapezoidal_difference:<16.8f}  {simpson_difference:<16.8f}")
