from stats import get_num_words, count_characters, sort_characters
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    chars = count_characters(book_text)
    sorted_chars = sort_characters(chars)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print(chars)

main()
