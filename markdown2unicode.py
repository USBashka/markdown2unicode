import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

import pyperclip

from converter import convert



def main():
    def on_convert_pressed():
        result = convert(window.input_text.toPlainText())
        window.result.setPlainText(result)
        pyperclip.copy(result)
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    window = loader.load("ui.ui", None)
    window.convert.clicked.connect(on_convert_pressed)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()