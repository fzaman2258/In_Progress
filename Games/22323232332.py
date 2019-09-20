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



'''

display_string = ''.join(list_letters_remaining)  # This prints  ----  and will update as user plays
current_state = QLabel(display_string)            #
submit_button = QPushButton('Submit')
enter = QLineEdit('')
temp = enter.text()
letter = submit_button.clicked.connect(partial(submit_button_clicked,temp))
label2 = QLabel("You only have "+ str(len(word))+ " guesses remaining! "+" Letters already inputted:a "+ str(letters_input))
layout = QVBoxLayout()
layout.addWidget(label2)
layout.addWidget(current_state)
layout.addWidget(QLabel("Enter a letter: "))
layout.addWidget(enter)
layout.addWidget(submit_button)
window.setLayout(layout)
window.show()
'''


display_string = ''.join(list_letters_remaining)  # This prints  ----  and will update as user plays
current_state = QLabel(display_string)            #
submit_button = QPushButton('Submit')

enter = QLineEdit('')


label2 = QLabel("You only have " + str(len(word)) + " guesses remaining! "+" Letters already inputted:a "+ str(letters_input))
layout = QVBoxLayout()
layout.addWidget(label2)
layout.addWidget(current_state)
layout.addWidget(QLabel("Enter a letter: "))
layout.addWidget(enter)
layout.addWidget(submit_button)
window.setLayout(layout)
window.show()
for i in range(0,3):
    label2.setText('change'+str(i))
    window.update()
app.exec()
