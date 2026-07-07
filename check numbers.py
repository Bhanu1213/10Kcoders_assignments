# ================== 1. Sum of Digits ==================

num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit
    temp //= 10

print("Sum =", sum)


# ================== 2. Reverse a Number ==================

num = int(input("Enter a number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reverse =", reverse)


# ================== 3. Count Digits ==================

num = int(input("Enter a number: "))
temp = num
count = 0

while temp > 0:
    count += 1
    temp //= 10

print("Digits =", count)


# ================== 4. Even or Odd ==================

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# ================== 5. Prime Number ==================

num = int(input("Enter a number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")


# ================== 6. Factorial ==================

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)


# ================== 7. Factors of a Number ==================

num = int(input("Enter a number: "))

print("Factors:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print()


# ================== 8. Palindrome Number ==================

num = int(input("Enter a number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# ================== 9. Armstrong Number ==================

num = int(input("Enter a number: "))
temp = num
length = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10

if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")


# ================== 10. GCD (HCF) ==================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD =", a)
