#!/usr/bin/python3
"""
Function that calculates the min operations to copy and paste letters
"""

def minOperations(n):
    if n == 1:
        return 0

    # Helper function to check if a number is prime
    def is_prime(num):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Helper function to find the smallest divisor
    def smallest_divisor(num):
        for i in range(2, num + 1):
            if num % i == 0:
                return i

    # Initialize the number of operations
    operations = 0

    while n > 1:
        # If n is prime, paste n times
        if is_prime(n):
            operations += n
            break
        else:
            # Find the smallest divisor and paste that many times
            divisor = smallest_divisor(n)
            operations += divisor
            n //= divisor

    return operations

# Example usage
n = 9
result = minOperations(n)
print(f"Number of operations for n={n}: {result}")

