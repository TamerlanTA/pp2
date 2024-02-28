def replace_with_colon(text):
    # Replace space, comma, and dot with colon
    modified_text = text.replace(' ', ':').replace(',', ':').replace('.', ':')
    return modified_text
f = open("row.txt", "r")
def main():
    text = f.read()
    modified_text = replace_with_colon(text)
    print("Modified string:", modified_text)

if __name__ == "__main__":
    main()
