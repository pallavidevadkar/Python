S = "I am pallavi, I am CSE student at DYPCET"
vowels = "AEIOUaeiou"
count = 0
for char in S:
    if char in vowels:
        count += 1
print("Number of vowels in string S : ", count)