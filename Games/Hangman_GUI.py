import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime, Qt, QTimer
from functools import partial


def submit_button_clicked():

    entered_letter = enter.text()
    entered_letter = entered_letter.lower()
    enter.setText('')
    return entered_letter


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

letters_remaining = len(word)

guesses = 0
won = False
list_letters_remaining = []
letters_input = []

for i in range(0, len(word)):
    list_letters_remaining.append(" _ ")


app = QApplication([])
window = QWidget()
display_string = ''.join(list_letters_remaining)  # This prints  ----  and will update as user plays
current_state = QLabel(display_string)            #
submit_button = QPushButton('Submit')
enter = QLineEdit('')
label2 = QLabel("You only have " + str(len(word)) + " guesses remaining! "+" Letters already inputted:a "+ str(letters_input))
layout = QVBoxLayout()
submit_button.clicked.connect(submit_button_clicked)
letter = submit_button_clicked()
layout.addWidget(label2)
layout.addWidget(current_state)
layout.addWidget(QLabel("Enter a letter: "))
layout.addWidget(enter)
layout.addWidget(submit_button)
window.setLayout(layout)

while guesses < 9:
    display_string = ''.join(list_letters_remaining)
    current_state.setText(display_string)
    if letters_remaining == 0:
        won = True
        break
    remain = 9-guesses
    label2.setText("You only have " + str(remain) + " guesses remaining! "+" Letters already inputted:a "+ str(letters_input))
    window.update()

    submit_button.clicked.connect(submit_button_clicked)
    letter = submit_button_clicked()

    if letter in letters_input:
        error_1 = QLabel("You have already entered this letter! \033[0;31;40m")
        layout.addWidget(error_1)
        window.setLayout(layout)
        window.update()
    elif letter.isalpha() is False:
        error_2 = QLabel("You can only enter letters! \033[0;31;40m")
        layout.addWidget(error_2)
        window.setLayout(layout)
        window.update()
    elif len(letter) > 1:
        error_3 = QLabel("Only one letter at a time! \033[0;31;40m")
        layout.addWidget((error_3))
        window.setLayout(layout)
        window.update()
    elif wrong(letter) is True:
        guesses += 1
        letters_input.append(letter)
    else:
        letters_remaining = print_curr_state(word, letter, letters_remaining, list_letters_remaining)
        letters_input.append(letter)

if won:
    layout.addWidget(QLabel("GG YOU WON"))
    window.setLayout(layout)
    window.update()
else:
    layout.addWidget(QLabel('GG YOU LOST'))
    window.setLayout(layout)
    window.update()
window.show()

app.exec()

