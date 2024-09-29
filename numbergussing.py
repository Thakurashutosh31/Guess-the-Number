import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class NumberGuessingGame(QWidget):
    def __init__(self):
        super().__init__()

        self.random_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Guess the Number")
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Enter your guess:")
        layout.addWidget(self.label)

        self.guess_entry = QLineEdit()
        layout.addWidget(self.guess_entry)

        self.guess_button = QPushButton("Guess")
        self.guess_button.clicked.connect(self.guess)
        layout.addWidget(self.guess_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def guess(self):
        guess = int(self.guess_entry.text())
        self.guess_entry.clear()

        self.attempts += 1

        if guess > self.random_number:
            self.result_label.setText("Too high!")
        elif guess < self.random_number:
            self.result_label.setText("Too low!")
        else:
            self.result_label.setText("Correct!")

        if self.attempts < self.max_attempts and guess != self.random_number:
            self.result_label.setText("")

        if self.attempts == self.max_attempts and guess != self.random_number:
            self.result_label.setText("Sorry, you didn't guess the number. The number was " + str(self.random_number))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = NumberGuessingGame()
    game.show()
    sys.exit(app.exec_())