
def get_num_words(text):
    return len(text.split())

def count_characters(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_characters(chars):
    list_chars = [{"char": c, "num": n} for c, n in chars.items()]
    list_chars.sort(key=lambda x: x["num"], reverse=True)
    return list_chars
