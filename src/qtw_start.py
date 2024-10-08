import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Tracker")
        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("This is my tracker. Enter your data below:")

        my_label.setFont(qtg.QFont('Helvetica', 18))    

        self.layout().addWidget(my_label)

        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setPlaceholderText("Enter your name")
        self.layout().addWidget(my_entry)

        def press_it():
            my_label.setText(f"Hello, {my_entry.text()}")
            my_entry.setText("")

        my_button = qtw.QPushButton("Submit", clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()