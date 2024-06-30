import sys

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        words = text.split()
        word_count = len(words)
        return word_count
    except FileNotFoundError:
        return "File not found."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        filename = sys.argv[1]
        print(f"The number of words in {filename} is {count_words_in_file(filename)}.")

