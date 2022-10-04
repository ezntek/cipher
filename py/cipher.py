def find_index(char: str) -> int:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i, c in enumerate(alphabet):
        if c == char:
            return i
    return 26

def shift_alphabet(by: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[by:] + alphabet[0:by]

def cipher(text: str, key: str) -> str:
    retval = ""
    table = [shift_alphabet(i) for i in range(26)]
    for text_c, key_c in zip(text, key):
        try:
            retval += table[find_index(text_c.lower())][find_index(key_c.lower())]
        except IndexError:
            retval += text_c
    return retval
