import pandas as pd


def main():
    alphabet = pd.read_csv('day-26-nato_phonetic_alphabet.csv')
    nato_alphabet = {row.letter: row.code for (index, row) in alphabet.iterrows()}

    user_input = input('Enter a word: ').upper()
    nato_code = [nato_alphabet[letter] for letter in user_input]
    print(nato_code)


if __name__ == '__main__':
    main()
