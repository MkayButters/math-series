def fibonacci(n):
    p1, p2 = 0,1
    for i in range(n-2):
        p3 = p1+p2
        p1 = p2
        p2 = p3
    return p3

def lucas(n):
        p1, p2 = 2,1
    for i in range(n-2):
        p3 = p1+p2
        p1 = p2
        p2 = p3
    return p3

def sum_series(n,a,g)
    
    a, g = 0, 1
    