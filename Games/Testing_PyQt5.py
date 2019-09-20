from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime, Qt, QTimer
from functools import partial

def ok(count):
    if count == 1:
        label2. setText("this changed")
        window.update()
    if count == 2:
        label2. setText("this changed AGAINNNNNNNNNN")
        window.update()

list_letters_remaining = []
for i in range(0, 9):
    list_letters_remaining.append(" _ ")
temp= ''.join(list_letters_remaining)

app = QApplication([])

label = QLabel(temp)
global label2
label2 = QLabel('hahaha')


window = QWidget()

button = QPushButton('Submit');
count = 1;
button.clicked.connect(partial(ok,count))
count = 2;
button.clicked.connect(partial(ok,count))

button2 =QPushButton("Submit again")
button2.clicked.connect(partial(ok,label2))

layout = QHBoxLayout()

layout.addWidget(QLabel('Enter your word'))
layout.addWidget(QLineEdit(''))
layout.addWidget(button)
layout.addWidget(button2)
layout.addWidget(QCheckBox("Check if "))
layout.addWidget(label)
layout.addWidget(label2)

window.setLayout(layout)
window.show()


app.exec()

if won:
    layout.addWidget(QLabel("GG YOU WON"))
    window.setLayout(layout)
    window.update()
else:
    layout.addWidget(QLabel('GG YOU LOST'))
    window.setLayout(layout)
    window.update()
