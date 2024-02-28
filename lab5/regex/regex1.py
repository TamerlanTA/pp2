import re

def match_pattern(text):
    pattern = r'ab*'
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

f = open("row.txt", "r")
text_to_match = f.read()
if match_pattern(text_to_match):
    print("The string matches the pattern.")
else:
    print("The string does not match the pattern.")
