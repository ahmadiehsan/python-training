def remove_non_ascii_characters(sentence):
    return sentence.encode('ascii', 'ignore').decode('UTF8')
