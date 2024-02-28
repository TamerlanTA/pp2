import re

def find_sequences(text):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    return pattern.findall(text)

f = open("row.txt", "r")
text_to_search = f.read()
sequences = find_sequences(text_to_search)
if sequences:
    print("Sequences found:", sequences)
else:
    print("No sequences found.")
