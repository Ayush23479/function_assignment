
#  using recurssion

def facto(n):
    if n == 1 or n == 0:
        return 1
    else: 
        return n*facto(n-1)

print(facto(6))


# using loops

def factorial(num):
    i = num
    factor = 1
    while i>0:
        factor *= i
        i -= 1
    print("Factorial of",num,":", factor)

factorial(0)