#!/usr/bin/python3

import string as s
import random as r
import sys


help_message = """
ERROR!


r-passgen:  A password generator utility


Usage: 
    ./r-passgen.py [special] [numbers] [lowercase] [uppercase]

Where:
    special   - number of special chars in the password
    numbers   - number of special chars in the password
    lowercase - number of special chars in the password
    uppercase - number of special chars in the password

"""


class PassGen:
    def __init__(self, qtd_special=2, qtd_numbers=2, qtd_lowercase=2, qtd_uppercase=2):
        self.qtd_special = qtd_special
        self.qtd_numbers = qtd_numbers
        self.qtd_lowercase = qtd_lowercase
        self.qtd_uppercase = qtd_uppercase

        self.special = list(s.punctuation)
        self.numbers = list(s.digits)
        self.lowercase = list(s.ascii_lowercase)
        self.uppercase = list(s.ascii_uppercase)

    def generate(self):
        choosen_special = [
            self.special[r.randint(0, len(self.special) - 1)]
            for char in range(0, self.qtd_special)
        ]
        choosen_numbers = [
            self.numbers[r.randint(0, len(self.numbers) - 1)]
            for char in range(0, self.qtd_numbers)
        ]
        choosen_lowercase = [
            self.lowercase[r.randint(0, len(self.lowercase) - 1)]
            for char in range(0, self.qtd_lowercase)
        ]
        choosen_uppercase = [
            self.uppercase[r.randint(0, len(self.uppercase) - 1)]
            for char in range(0, self.qtd_uppercase)
        ]
        password = (
            choosen_special + choosen_numbers + choosen_lowercase + choosen_uppercase
        )
        password = "".join(r.sample(password, len(password)))
        return password


if __name__ == "__main__":
    if len(sys.argv) >= 5:
        try:
            print(
                PassGen(
                    int(sys.argv[1]),
                    int(sys.argv[2]),
                    int(sys.argv[3]),
                    int(sys.argv[4]),
                ).generate()
            )
        except:
            sys.exit(help_message)
    else:
        sys.exit(help_message)
