import string
import random

LETTERS = string.ascii_letters
DIGIT = string.digits
PUNCTUATION = string.punctuation
PRINTABLE = f"{LETTERS}{DIGIT}{PUNCTUATION}"
PRINTABLE = list(PRINTABLE)
random.shuffle(PRINTABLE)

def password_generator(length:int = 8):
    random_password = random.choices(PRINTABLE, k = length)
    return "".join(random_password)

def main():
    # print(PRINTABLE)
    print(password_generator())

if __name__ == "__main__":
    main()