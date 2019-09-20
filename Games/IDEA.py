import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime, Qt, QTimer
from functools import partial


def submit_button_clicked(layout,word,letters_remaining,letters_input,guesses,list_letters_remaining):
    if letters_remaining == 0:
        layout_2 =QVBoxLayout()
        win_label =QLabel("GG YOU WON")
        layout_2.addWidget(win_label)
        window.setLayout(layout_2)
        window.update()
    if guesses == 9:
        layout_2 =QVBoxLayout()
        lost_label =QLabel("GG YOU LOST")
        layout_2.addWidget(lost_label)
        window.setLayout(layout_2)
        window.update()

    letter = enter.text()
    letter = letter.lower()
    enter.setText('')
    display_string = ''.join(list_letters_remaining)
    current_state.setText(display_string)
    remain = 9-guesses
    label2.setText("You only have " + str(remain) + " guesses remaining! "+" Letters already inputted:a "+ str(letters_input))
    window.update()

    if letter in letters_input:
        error_1 = QLabel("You have already entered this letter! \033[0;31;40m")
        layout.addWidget(error_1)
        window.setLayout(layout)
        window.update()
        layout.removeWidget(error_1)
    elif letter.isalpha() is False:
        error_2 = QLabel("You can only enter letters! \033[0;31;40m")
        layout.addWidget(error_2)
        window.setLayout(layout)
        window.update()
        layout.removeWidget(error_2)
    elif len(letter) > 1:
        error_3 = QLabel("Only one letter at a time! \033[0;31;40m")
        layout.addWidget(error_3)
        window.setLayout(layout)
        window.update()
        layout.removeWidget(error_3)
    elif wrong(letter) is True:
        guesses += 1
        letters_input.append(letter)
        error_4 = QLabel("WRONG! \033[0;31;40m")
        layout.addWidget(error_4)
        window.setLayout(layout)
        window.update()
        layout.removeWidget(error_4)
    else:
        letters_remaining = print_curr_state(word, letter, letters_remaining, list_letters_remaining)
        letters_input.append(letter)
        good_job = QLabel("GOOD JOB")
        layout.addWidget(good_job)
        window.update()
        layout.removeWidget(good_job)


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
display_string = ''.join(list_letters_remaining)
current_state = QLabel(display_string)
submit_button = QPushButton('Submit')
enter = QLineEdit('')
label2 = QLabel("You only have " + str(9) + " guesses remaining! "+" Letters already inputted:a "+ str(letters_input))
layout = QVBoxLayout()
layout.addWidget(label2)
layout.addWidget(current_state)
layout.addWidget(QLabel("Enter a letter: "))
layout.addWidget(enter)
layout.addWidget(submit_button)
window.setLayout(layout)

submit_button.clicked.connect(partial(submit_button_clicked,layout,word,letters_remaining,letters_input,guesses,list_letters_remaining))

window.show()
app.exec()