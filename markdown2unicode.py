import sys
import webbrowser

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
import pyperclip

from converter import convert



def main():
    def on_convert_pressed():
        if window.input_text.toPlainText():
            result = convert(window.input_text.toPlainText())
            window.result.setPlainText(result)
            pyperclip.copy(result)
            window.statusbar.showMessage("Text copied to clipboard")
        else:
            window.statusbar.showMessage("Write text first")
    
    def on_help_pressed():
        webbrowser.open("https://www.markdownguide.org/basic-syntax/#emphasis")
    
    def on_input_text_edited():
        window.statusbar.showMessage("")
    

    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    window = loader.load("ui.ui", None)
    window.input_text.textChanged.connect(on_input_text_edited)
    window.help.clicked.connect(on_help_pressed)
    window.convert.clicked.connect(on_convert_pressed)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
