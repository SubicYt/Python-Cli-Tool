def main():
    book_path = "Books/frankenstein.txt"
    txt = get_book_text(book_path)
    print (txt)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()