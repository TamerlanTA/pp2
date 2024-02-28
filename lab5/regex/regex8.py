import re

def split_at_uppercase(text):
    # Split the string at uppercase letters
    parts = re.findall('[A-Z][^A-Z]*', text)
    return parts
f = open("row.txt", "r")
def main():
    text = f.read()
    parts = split_at_uppercase(text)
    print("Parts after splitting at uppercase letters:", parts)

if __name__ == "__main__":
    main()
