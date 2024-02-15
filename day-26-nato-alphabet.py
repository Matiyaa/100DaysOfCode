import pandas as pd


def main():
    alphabet = pd.read_csv('day-26-nato_phonetic_alphabet.csv')
    nato_alphabet = {row.letter: row.code for (index, row) in alphabet.iterrows()}
    generate_nato_code(nato_alphabet)


def generate_nato_code(nato_alphabet):
    user_input = input('Enter a word: ').upper()

    try:
        nato_code = [nato_alphabet[letter] for letter in user_input]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_nato_code(nato_alphabet)
    else:
        print(nato_code)


if __name__ == '__main__':
    main()
