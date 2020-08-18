import string


alphabet = string.ascii_lowercase

def encode_caesar(string='test',rot=1):
    final_string = ''
    for el in string:
        index = alphabet.find(el)
        final_string += alphabet[index + rot]
    return final_string
