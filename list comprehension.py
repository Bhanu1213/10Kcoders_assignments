
st= "hi hello raju"
vowels = [ch for ch in st if ch.lower() in "aeiou"]
consonants = [ch for ch in st if ch.isalpha() and ch.lower() not in "aeiou"]
print("Vowels:", vowels)
print("Consonants:", consonants)
