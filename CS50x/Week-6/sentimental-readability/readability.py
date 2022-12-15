from cs50 import get_string


def main():
    text = get_string("Text: ")
    length = len(text)

    letters = count_letters(text, length)
    words = count_words(text, length)
    sentences = count_sentences(text, length)

    l = 100 * letters / words
    s = 100 * sentences / words

    index = 0.0588 * l - 0.296 * s - 15.8
    cli = round(index)

    if cli < 1:
        print("Before Grade 1")

    if cli in range(2, 16):
        print(f"Grade {cli}")

    if cli > 15:
        print("Grade 16+")


def count_letters(text, length):
    counter = 0
    for i in range(length):
        if text[i].lower() >= 'a' and text[i].lower() <= 'z':
            counter += 1

    return counter


def count_words(text, length):
    counter = 1
    for i in range(length):
        if text[i] == ' ':
            counter += 1

    return counter


def count_sentences(text, length):
    counter = 0

    for i in range(length):
        if text[i] == '!' or text[i] == '.' or text[i] == '?':
            counter += 1

    return counter


main()