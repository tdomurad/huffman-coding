f = open("test.txt", "r")
text = f.read()
f.close()

frequency = [0] * 256

letters = []

for letter in text:
    frequency[ord(letter)] += 1
    letters.append(letter)

letters = sorted(set(letters))

frequency = [x for x in frequency if x != 0]

print(letters)
print(frequency)


