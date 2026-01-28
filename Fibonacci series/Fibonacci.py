def fibonacci_recursive(n):
    # Base Case: If n is 0 or 1, return n
    if n <= 1:
        return n
    else:
        # Recursive Step: F(n) = F(n-1) + F(n-2)
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# User Input
terms = int(input("How many terms? "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(terms):
        print(fibonacci_recursive(i), end=" ")