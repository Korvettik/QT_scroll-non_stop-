#!/usr/bin/python3

import sys, random
from PyQt5.QtWidgets import QApplication, QListWidget


class infinite_scroll_area(QListWidget):  # https://doc.qt.io/qt-5/qlistwidget.html
    def __init__(self):
        super().__init__()  # call the parent constructor if you're overriding it.
        # connect our own function the valueChanged event
        self.verticalScrollBar().valueChanged.connect(self.valueChanged)
        self.add_lines(15)
        self.show()

    def valueChanged(self, value):  # https://doc.qt.io/qt-5/qabstractslider.html#valueChanged
        if value == self.verticalScrollBar().maximum():  # if we're at the end
            self.add_lines(5)

    def add_lines(self, n):
        for _ in range(n):  # add random lines
            line_text = str(random.randint(0, 100)) + ' some data'
            self.addItem(line_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = infinite_scroll_area()
    sys.exit(app.exec_())