def get_sentence():
    user_sentence = input('Please enter your message: ')
    return user_sentence


def ask_for_counting_non_ascii_characters():
    user_answer = bool(input('Count non ascii characters? [Left blank for no or enter a word for yes] '))
    return user_answer
