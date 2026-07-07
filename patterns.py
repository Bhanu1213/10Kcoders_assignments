# ================== 1. Square Pattern ==================

for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()


# ================== 2. Right Triangle ==================

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# ================== 3. Number Triangle ==================

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ================== 4. Repeated Number Triangle ==================

for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


# ================== 5. Alphabet Triangle ==================

for i in range(1, 6):
    ch = 'A'
    for j in range(i):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)
    print()


# ================== 6. Inverted Star Triangle ==================

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# ================== 7. Inverted Number Triangle ==================

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ================== 8. Continuous Number Pattern ==================

num = 1

for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# ================== 9. Right-Aligned Star Triangle ==================

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


# ================== 10. Pyramid Pattern ==================

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
