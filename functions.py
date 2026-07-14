
#calculator for num

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Invalid operator"

print(calculate(10, 5, '+'))  # Output: 15


#palindrome number

def is_palindrome(text):
    # Clean the string: remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# Example Usage
print(is_palindrome("Racecar"))      # Output: True
print(is_palindrome("Hello World"))  # Output: False


# factorial of a number

def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example Usage
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1


# prime number

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example Usage
print(is_prime(17))  # Output: True
print(is_prime(10))  # Output: False


#filter evens in the list

def filter_evens(numbers):
    return [num for num in numbers if num % 2 == 0]

# Example Usage
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_evens(nums))  # Output: [2, 4, 6, 8, 10]


#count vowels in a text
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Example Usage
print(count_vowels("Hello World"))   # Output: 3
print(count_vowels("Python"))        # Output: 1
print(count_vowels("AEIOU"))         # Output: 5