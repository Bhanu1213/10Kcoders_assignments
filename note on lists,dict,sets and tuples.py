# ================== LIST ==================

list1 = [10, 20, 30, 40]

print("List:", list1)
print("First Element:", list1[0])

list1.append(50)
list1.insert(1, 15)
list1.remove(20)
list1.pop()

print("Updated List:", list1)


# ================== NESTED LIST ==================

students = [
    ["Rahul", 20],
    ["Priya", 21],
    ["Arun", 22]
]

print("\nNested List:", students)
print("First Row:", students[0])
print("First Student Name:", students[0][0])


# ================== TUPLE ==================

tuple1 = (10, 20, 30, 20)

print("\nTuple:", tuple1)
print("First Element:", tuple1[0])
print("Length:", len(tuple1))
print("Count of 20:", tuple1.count(20))
print("Index of 30:", tuple1.index(30))


# ================== SET ==================

set1 = {10, 20, 30, 20}

print("\nSet:", set1)

set1.add(40)
set1.remove(20)

print("Updated Set:", set1)

A = {1, 2, 3}
B = {3, 4, 5}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
print("Symmetric Difference:", A ^ B)


# ================== DICTIONARY ==================

student = {
    "name": "Rahul",
    "age": 20,
    "marks": 90
}

print("\nDictionary:", student)
print("Name:", student["name"])
print("Age:", student["age"])

student["age"] = 21
student["city"] = "Hyderabad"

student.pop("marks")

print("Updated Dictionary:", student)
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
