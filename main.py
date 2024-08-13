def main():
    book_path = "Books/frankenstein.txt"
    txt = get_book_text(book_path)
    print (txt)
    num_words = get_num_words(txt)
    print(f"There are {num_words} words in this doc")
    print(f"This book has {get_num_letters(txt)} letters")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(txt):
    words = txt.split()
    return len(words)


def get_num_letters(text):
    dict_of_letters = {}
    words = text.split(" ")
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter.isalpha():
                if letter in dict_of_letters:
                    dict_of_letters[letter] += 1
                else: 
                    dict_of_letters[letter] = 1
    return dict_of_letters
main()