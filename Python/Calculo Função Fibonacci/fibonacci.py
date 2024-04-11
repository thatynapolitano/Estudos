def Fibonacci(N):
    if N == 0: 
        return 0
    elif N == 1:
        return 1
    else: 
        return Fibonacci(N-1)+ Fibonacci(N-2)

print(Fibonacci(5))
print(Fibonacci(6))
print(Fibonacci(7))