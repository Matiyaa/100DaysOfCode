def main():
    names = []
    with open('day-24-invited-names.txt') as file:
        names = file.read().splitlines()

    letter = ''
    with open('day-24-starting_letter.txt') as file:
        letter = file.read()

    output = ''
    for name in names:
        output += letter.replace('[name]', name)
        output += '\n'

    with open('day-24-output.txt', mode='w') as file:
        file.write(output)

    print(output)


if __name__ == '__main__':
    main()