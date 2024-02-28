import re

def match_pattern(text):
    pattern = r'^a.*b$'
    if re.match(pattern, text):
        return True
    else:
        return False
f = open("row.txt", "r")
def main():
    text = f.read()
    if match_pattern(text):
        print("The string matches the pattern.")
    else:
        print("The string does not match the pattern.")

if __name__ == "__main__":
    main()
