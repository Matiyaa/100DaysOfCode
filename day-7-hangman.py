import random


def main():
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

    word_list = [
        'abruptly',
        'absurd',
        'abyss',
        'affix',
        'askew',
        'avenue',
        'awkward',
        'axiom',
        'azure',
        'bagpipes',
        'bandwagon',
        'banjo',
        'bayou',
        'beekeeper',
        'bikini',
        'blitz',
        'blizzard',
        'boggle',
        'bookworm',
        'boxcar',
        'boxful',
        'buckaroo',
        'buffalo',
        'buffoon',
        'buxom',
        'buzzard',
        'buzzing',
        'buzzwords',
        'caliph',
        'cobweb',
        'cockiness',
        'croquet',
        'crypt',
        'curacao',
        'cycle',
        'daiquiri',
        'dirndl',
        'disavow',
        'dizzying',
        'duplex',
        'dwarves',
        'embezzle',
        'equip',
        'espionage',
        'exodus',
        'faking',
        'fishhook',
        'fixable',
        'fjord',
        'flapjack',
        'flopping',
        'fluffiness',
        'flyby',
        'foxglove',
        'frazzled',
        'frizzled',
        'fuchsia',
        'funny',
        'gabby',
        'galaxy',
        'galvanize',
        'gazebo',
        'gizmo',
        'glowworm',
        'glyph',
        'gnarly',
        'gnostic',
        'gossip',
        'grogginess',
        'haiku',
        'haphazard',
        'hyphen',
        'iatrogenic',
        'icebox',
        'injury',
        'ivory',
        'ivy',
        'jackpot',
        'jaundice',
        'jawbreaker',
        'jaywalk',
        'jazziest',
        'jazzy',
        'jelly',
        'jigsaw',
        'jinx',
        'jiujitsu',
        'jockey',
        'jogging',
        'joking',
        'jovial',
        'joyful',
        'juicy',
        'jukebox',
        'jumbo',
        'kayak',
        'kazoo',
        'keyhole',
        'khaki',
        'kilobyte',
        'kiosk',
        'kitsch',
        'kiwifruit',
        'klutz',
        'knapsack',
        'larynx',
        'lengths',
        'lucky',
        'luxury',
        'lymph',
        'marquis',
        'matrix',
        'megahertz',
        'microwave',
        'mnemonic',
        'mystify',
        'naphtha',
        'nightclub',
        'nowadays',
        'numbskull',
        'nymph',
        'onyx',
        'ovary',
        'oxidize',
        'oxygen',
        'pajama',
        'peekaboo',
        'phlegm',
        'pixel',
        'pizazz',
        'pneumonia',
        'polka',
        'pshaw',
        'psyche',
        'puppy',
        'puzzling',
        'quartz',
        'queue',
        'quips',
        'quixotic',
        'quiz',
        'quizzes',
        'quorum',
        'razzmatazz',
        'rhubarb',
        'rhythm',
        'rickshaw',
        'schnapps',
        'scratch',
        'shiv',
        'snazzy',
        'sphinx',
        'spritz',
        'squawk',
        'staff',
        'strength',
        'strengths',
        'stretch',
        'stronghold',
        'stymied',
        'subway',
        'swivel',
        'syndrome',
        'thriftless',
        'thumbscrew',
        'topaz',
        'transcript',
        'transgress',
        'transplant',
        'twelfth',
        'twelfths',
        'unknown',
        'unworthy',
        'unzip',
        'uptown',
        'vaporize',
        'vixen',
        'vodka',
        'voodoo',
        'vortex',
        'voyeurism',
        'walkway',
        'waltz',
        'wave',
        'wavy',
        'waxy',
        'wellspring',
        'wheezy',
        'whiskey',
        'whizzing',
        'whomever',
        'wimpy',
        'witchcraft',
        'wizard',
        'woozy',
        'wristwatch',
        'wyvern',
        'xylophone',
        'yachtsman',
        'yippee',
        'yoked',
        'youthful',
        'yummy',
        'zephyr',
        'zigzag',
        'zigzagging',
        'zilch',
        'zipper',
        'zodiac',
        'zombie',
    ]

    logo = ''' 
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/    '''

    lives = 6

    print(logo)

    word = random.choice(word_list)

    display = ["_" for _ in word]

    playing = True
    guesses = []

    while playing:
        print(stages[lives])
        print(''.join(display))

        if guesses:
            print(f"Previous guesses: {''.join(guesses)}")

        guess = input("Guess a letter: ").lower()

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            guesses.append(guess)
            print("Wrong")

        if "_" not in display:
            print("You win!")
            playing = False
        elif guess not in word:
            lives -= 1

        if lives == 0:
            print("You lose!")
            print(f"The word was {word}")
            playing = False


if __name__ == "__main__":
    main()
