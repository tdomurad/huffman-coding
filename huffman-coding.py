class Node:
    def __init__(self, letter, frequency, left=None, right=None):
        self.letter = letter
        self.frequency = frequency
        self.left = left
        self.right = right
        self.value = ''


def set_values(node, value=''):
    value = value + str(node.value)

    if node.left:
        set_values(node.left, value)

    if node.right:
        set_values(node.right, value)

    if not node.left and not node.right:
        dictionary[node.letter] = value


def print_codes():
    for i in range(len(letters)):
        print(f"{letters[i]}:{frequency[i]}\t{dictionary[letters[i]]}")


# Read from file and save it to text
file_read = open("some_text.txt", "r")
text = file_read.read()
file_read.close()

# Initialize arrays for letters in file and their frequency
letters = []
frequency = [0] * 256
dictionary = {}

# For each letter add 1 to frequency index corresponding to letter's ASCII number and apeend letters array
for letter in text:
    frequency[ord(letter)] += 1
    letters.append(letter)

# Delete repeated letters and sort an array
letters = sorted(set(letters))

# Delete all letters with frequency equal to 0
frequency = [x for x in frequency if x != 0]

# Test if everything goes right

# print(letters)
# print(frequency)

# Create array of nodes
nodes = []
for i in range(len(letters)):
    nodes.append(Node(letters[i], frequency[i]))

count_created_nodes = 0

# coding
while len(nodes) > 1:
    # Sort by frequency
    nodes = sorted(nodes, key=lambda node: node.frequency)

    left = nodes.pop(0)
    right = nodes.pop(0)

    # Left node's code is 0, right one is 1
    left.value = 0
    right.value = 1

    nodes.append(Node('z' + str(count_created_nodes), left.frequency + right.frequency, left, right))

set_values(nodes[0])

# Sort dictionary
# dictionary = dict(sorted(dictionary.items(), key=lambda item: item[0]))

print_codes()

f = open("coded.txt", "w")
coded_text = ''
for letter in text:
    coded_text += dictionary[letter]
f.write(coded_text)
f.close()

f = open("decoded.txt", "w")
decoded_text = ''
temp_text = ''
for letter in coded_text:
    temp_text += letter

    for character, value in dictionary.items():
        if value == temp_text:
            decoded_text += character
            temp_text = ''

f.write(decoded_text)
f.close()