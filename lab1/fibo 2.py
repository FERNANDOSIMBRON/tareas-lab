def fib_r(n):
    a = 0
    b = 1
    
    for k in range(n):
        c = a + b 
        a = b
        b = c
    
    return b

for c in range(20):
    print(fib_r(c))