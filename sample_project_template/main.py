from sentence_digest import count_of_words
from sentence_filter import remove_non_ascii_characters
from user_input import get_sentence, ask_for_counting_non_ascii_characters


def main():
    sentence = get_sentence()

    count_non_ascii = ask_for_counting_non_ascii_characters()
    if not count_non_ascii:
        sentence = remove_non_ascii_characters(sentence)

    number_of_words = count_of_words(sentence)

    print(number_of_words)


main()
