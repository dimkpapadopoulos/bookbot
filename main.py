def word_count(string):
    return len(string.split())


def character_count(string):
    lower_str = string.lower()
    char_dict = {}
    for c in lower_str:
        if c.isalpha():
            if c not in char_dict:
                char_dict.update({c: 1})
            else:
                char_dict[c] += 1
    sorted_char_dict = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)
    for k,v in sorted_char_dict:
        print(f"The {k} character was found {v} times")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    words = word_count(file_contents)
    print(words,"words found in the document")
    character_count(file_contents)
    print("--- End report ---")

main()