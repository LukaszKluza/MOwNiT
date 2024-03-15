import math 

def e_to_x(x):
    e1, e2 = 0, 1
    iterator  = 1
    power = 1
    while e1 != e2:
        e1 = e2 
        e2 += (x**iterator)/power
        iterator += 1
        power *= iterator
    return e2
    

if __name__ == "__main__": 
    X = [1,-1,5,-5,10,-10, 100,-100]
    X_plus = [1,5,10,100]
    for x in X:
        print(f"e^{x}: {e_to_x(x)}, exp: ({math.exp(x)}) difference: {math.fabs(e_to_x(x)-math.exp(x))}")

    print("---------------------")    
    for x in X_plus:
        print(f"e^{x}: {e_to_x(x)}, exp: ({math.exp(x)}) difference: {math.fabs(e_to_x(x)-math.exp(x))}")
        print(f"e^{x}: {1/e_to_x(x)}, exp: ({math.exp(-x)}) difference: {math.fabs(1/e_to_x(x)-math.exp(-x))}")
