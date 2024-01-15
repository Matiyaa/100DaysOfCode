from string import ascii_lowercase


def main():
    print("Welcome to Caesar Cipher")
    print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
    restart = True

    while restart:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        # if direction == "encode":
        #     encrypt(text, shift)
        # elif direction == "decode":
        #     decrypt(text, shift)
        # else:
        #     print("Invalid input")

        print(caesar(text, shift, direction))

        check = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if check == "no":
            print("Goodbye")
            restart = False

# def encrypt(text, shift):
#     new_text = ""
#     alphabet = ascii_lowercase
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_text += alphabet[new_position]
#     return new_text


# def decrypt(text, shift):
#     new_text = ""
#     alphabet = ascii_lowercase
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         new_text += alphabet[new_position]
#     return new_text


def caesar(text, shift, direction):
    new_text = ""
    alphabet = ascii_lowercase
    if direction == "decode":
        shift *= -1
    for character in text:
        if character in alphabet:
            position = alphabet.index(character)
            new_position = position + shift
            new_position = new_position % len(alphabet)
            new_text += alphabet[new_position]
        else:
            new_text += character
    return new_text


if __name__ == "__main__":
    main()
