def square(n):
    for i in range (1 , n+1):
        yield i ** 2
        
n = int(input())
for sq in square(n):
    print(sq)