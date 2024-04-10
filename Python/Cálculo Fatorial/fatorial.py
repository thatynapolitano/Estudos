def fatorial(N):
    if N < 0: 
        return None
    elif N == 0:
        return 1
    else:
        fat = 1 
        for i in range(1,N+1):
            fat *= i 
        return fat
    

print(fatorial(4))

# Fatorial de 4 =  4*3*2*1

 