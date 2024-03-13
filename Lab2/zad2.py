X_big = [1,5,10,15]
Y_big = [1,3,12,20]

X_small = [0.5,0.05,0.005,0.0005]
Y_small = [0.5,0.04,0.001,0.0006]

for x, y in zip(X_big, Y_big):
    print(x**2-y**2,"  ",(x-y)*(x+y), "  ", abs(x**2-y**2 - (x-y)*(x+y)))
    
print("------------------------------")

for x, y in zip(X_small, Y_small):
    print(x**2-y**2,"  ",(x-y)*(x+y), "  ", abs(x**2-y**2 - (x-y)*(x+y)))