from typing import List

count: int = 0          # number of matches found
List4: List[str] = []   # collection of all the 4-letter words
List16: List[str] = []  # collection of all the 16-letter words

with open("XwiJeffChenList.txt") as f:
    lines: List[str] = f.readlines()

# Read the file and collect all the 4- and 16-letter words

for line in lines:
    line = line.lower().strip()
    parts: List[str] = line.split(';')
    word: str = parts[0]  # Get the first part of the line, the word before ";"

    if len(word) == 4:
        List4.append(word)
    elif len(word) == 16:
        List16.append(word)

# Loop through all the 16-letter words. Break each down into quarters,
# and print it out if each part is a known 4-letter word.

for word16 in List16:
    part1: str = word16[0:4]
    part2: str = word16[4:8]
    part3: str = word16[8:12]
    part4: str = word16[12:16]

    if part1 in List4 and part2 in List4 and part3 in List4 and part4 in List4:
        print(f'{part1}-{part2}-{part3}-{part4} = {word16}')
        count += 1

print(f'{count} found')