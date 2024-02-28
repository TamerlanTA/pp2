import re

def match_pattern(text):
    pattern = re.compile(r'^ab{2,3}$')
    return bool(pattern.match(text))

f = open("row.txt", "r")
text_to_match = input()
if match_pattern(text_to_match):
    print("The string matches the pattern.")
else:
    print("The string does not match the pattern.")
