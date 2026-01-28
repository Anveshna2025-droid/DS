def factorial_recursion(n):
    if n==0 or n==1:
        return 1
    else :
        return n*factorial_recursion(n-1)
    
value=int(input("Enter a number for factorial finding:"))
print("Factorial of",value,"is:",factorial_recursion(value))
