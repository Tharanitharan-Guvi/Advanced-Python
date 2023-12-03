def fibonnaci(n):
    f1 = 0
    f2 = 1

    for i in range(1, n+1):
        yield f1
        f1, f2 = f2, f1+f2

for i in fibonnaci(10):
    print(i)