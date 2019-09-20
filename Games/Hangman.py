import random


def wrong(letter):
    if letter not in word:
        return True
    return False


def print_curr_state(word, letter, letters_remaining, list_letters_remaining):
    index = 0
    for char in word:
        if char == letter:
            list_letters_remaining[index] = letter
            letters_remaining -= 1
        index += 1
    return letters_remaining


# This part is just random list of words for the user to guess
list_of_words = ["appliances", "attic",  "backyard",  "barbecue", "baseboard", "basement", "bathroom", "bathtub",
                 "bedroom", "blinds", "broom", "bunk", "bed", "carpet", "car", "ceiling", "cellar", "chimney", "closet",
                 "clothes", "dryer", "washer", "concrete", "counter", "crib", "cupboard", "curtain", "rod"]
# Select a word from the list randomly doing math
r_num = random.randrange(0, len(list_of_words))
word = list_of_words[r_num]

letters_remaining = len(word)    # Initially its length of word and decrements every right letter inputted
guesses = 0                      # I will give 9 guesses for any word
won = False
list_letters_remaining = []
letters_input = []
# Make little visual in command line with underscores
for i in range(0, len(word)):
    list_letters_remaining.append(" _ ")
# Start the actual game and print updated visuals depending on flow
while guesses < 9:
    print()
    print("".join(list_letters_remaining))
    # Only way to win is to get all the letters
    if letters_remaining == 0:
        won = True
        break
    # Update user how many guesses left
    remain = 9-guesses
    print("You only have ", remain, " guesses remaining! ","Letters already inputted:a ", letters_input)

    # Words are not case-sensitive to lower everything
    letter = input("Enter your letter: ")
    letter = letter.lower()
    '''
        Here is the logic of hangman:
        1) Check if a letter has been already inputted
        2) Check if input is even a letter
        3) Check if letter is wrong via function
        Once all goes well, update the number of letters remaining by subtracting every place a letter is now being shown
        Update visual for user to see the current state
    '''

    if letter in letters_input:
        print()
        print("You have already entered this letter!")
    elif letter.isalpha() is False:
        print()
        print("You can only enter letters!")
    elif len(letter)>1 :
        print()
        print("Only one letter at a time!")
    elif wrong(letter) is True:
        guesses += 1
        letters_input.append(letter)
    else:
        letters_remaining = print_curr_state(word, letter, letters_remaining, list_letters_remaining)
        letters_input.append(letter)

if won:
    print("GG YOU WON")
else:
    print('GG YOU LOST')

