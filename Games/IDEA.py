import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime, Qt, QTimer
from functools import partial


def submit_button_clicked(layout,word,letters_remaining,letters_input,guesses,list_letters_remaining):   #If button clicked run game logic
    if letters_remaining == 0:                          # You entered all the right letters aka you won the game
        layout_2 =QVBoxLayout()
        win_label =QLabel("GG YOU WON")
        layout_2.addWidget(win_label)
        window.setLayout(layout_2)
        window.update()
        return
    if guesses == 9:                                    # We increment the guesses you have used thus far so you lost
        layout_3 =QVBoxLayout()
        lost_label =QLabel("GG YOU LOST")
        layout_3.addWidget(lost_label)
        window.setLayout(layout_3)
        window.update()
        return
    letter = enter.text().lower()                       # Game is not case sensitive, this works I checked by printing

    enter.setText('')                                   # Clear Line_Edit
    display_string = ''.join(list_letters_remaining)    # _ _ _ _ _ _  -> _ _ _ a _ _
    current_state.setText(display_string)
    remain = 9-guesses
    label2.setText("You only have " + str(remain) + " guesses remaining! "+" Letters already inputted:a "+ str(letters_input))
    window.setLayout(layout)
    window.update()

    if letter in letters_input:
        error_1 = QLabel("You have already entered this letter!")
        layout_4 =QVBoxLayout()
        layout_4.addWidget(error_1)
        window.setLayout(layout_4)
        window.update()
        layout_4.removeWidget(error_1)
    elif letter.isalpha() is False:
        error_2 = QLabel("You can only enter letters!")
        layout_5 =QVBoxLayout()
        layout_5.addWidget(error_2)
        window.setLayout(layout_5)
        window.update()
        layout_5.removeWidget(error_2)
    elif len(letter) > 1:
        error_3 = QLabel("Only one letter at a time!")
        layout_6 =QVBoxLayout()
        layout_6.addWidget(error_3)
        window.setLayout(layout_6)
        window.update()
        layout_6.removeWidget(error_3)
    elif wrong(letter) is True:
        guesses += 1
        letters_input.append(letter)
        error_4 = QLabel("WRONG!")
        layout_7 =QVBoxLayout()
        layout_7.addWidget(error_4)
        window.setLayout(layout_7)
        window.update()
        layout_7.removeWidget(error_4)
    else:
        letters_remaining = print_curr_state(word, letter, letters_remaining, list_letters_remaining)
        letters_input.append(letter)
        good_job = QLabel("GOOD JOB")
        layout_8 =QVBoxLayout()
        layout_8.addWidget(good_job)
        window.setLayout(layout_8)
        window.update()
        layout_8.removeWidget(good_job)
    return


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
label2 = QLabel("You only have " + str(9) + " guesses remaining! "+" Letters already inputted: "+ str(letters_input))
layout = QVBoxLayout()                                  # List GUI Vertically
layout.addWidget(label2)                                # First line says how many guesses remaining + letters inputted
layout.addWidget(current_state)                         # Displays the _ _ _ _ _ _
layout.addWidget(QLabel("Enter a letter: "))            # Just text
layout.addWidget(enter)                                 # Line Edit for them to enter their letter
layout.addWidget(submit_button)                         # A push_down button for them to click
window.setLayout(layout)                                # Attach everything to window

submit_button.clicked.connect(partial(submit_button_clicked,layout,word,letters_remaining,letters_input,guesses,list_letters_remaining))    # Every time button clicked do game logic

window.show()               # Show window for first time
app.exec()                  # Run GUI Logic