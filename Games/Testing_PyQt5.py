from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime, Qt, QTimer
from functools import partial

def ok(a):
    a.setText("this changed")
    window.update()

list_letters_remaining = []
for i in range(0, 9):
    list_letters_remaining.append(" _ ")
temp= ''.join(list_letters_remaining)

app = QApplication([])

label = QLabel(temp)
label2 = QLabel('hahaha')


window = QWidget()

button = QPushButton('Submit');
button.clicked.connect(partial(ok,label))

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
app.exec_()

