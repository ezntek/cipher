from cipher import cipher
from sys import argv

def main(args: list[str]):
    try:
        print(cipher(args[1], args[2]))
    except IndexError:
        print("simple cipher command line frontend for testing. please supply text to cipher.")

if __name__ == "__main__": main(argv)
