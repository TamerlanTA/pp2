import re

def find_sequences(text):
    pattern = r"[A-Z][a-z]+"
    sequences = re.findall(pattern, text)
    return sequences
f = open("row.txt", "r")
def main():
    text = f.read()
    sequences = find_sequences(text)
    if sequences:
        print("Sequences found:")
        for seq in sequences:
            print(seq)
    else:
        print("No sequences found.")

if __name__ == "__main__":
    main()
