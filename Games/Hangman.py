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

list_of_words = ["appliances", "attic",  "backyard",  "barbecue", "baseboard", "basement", "bathroom", "bathtub",
                 "bedroom", "blinds", "broom", "bunk", "bed", "carpet", "car", "ceiling", "cellar", "chimney", "closet",
                 "clothes", "dryer", "washer", "concrete", "counter", "crib", "cupboard", "curtain", "rod"]

r_num = random.randrange(0, len(list_of_words))

word = list_of_words[r_num]
letters_remaining = len(word)    # this is for when they guess the word right
guesses = 0                     # drawing the body
won = False
list_letters_remaining = []     #made  a list that I am printing out
letters_input = []

for i in range(0, len(word)):
    list_letters_remaining.append(" _ ")

while guesses < 9:
    print("".join(list_letters_remaining))

    if letters_remaining == 0:
       won = True
       break

    remain = 9-guesses
    print("You only have ", remain, " guesses remaining!")

    letter = input("Enter your letter: ")
    letter = letter.lower()

    if letter in letters_input:
        print("You have already entered this letter!")
    elif letter.isalpha() is False:
        print("You can only enter letters!")
    elif wrong(letter) is True:
        guesses += 1
    else:
        letters_remaining = print_curr_state(word, letter, letters_remaining, list_letters_remaining)
        letters_input.append(letter)

if won:
    print("GG YOU WON")
else:
    print('GG YOU LOST')