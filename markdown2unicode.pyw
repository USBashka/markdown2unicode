import sys, os

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
import pyperclip

from converter import convert


example = """**bold**
*italic*
***both***
`monospace`"""


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():

    # Event handlers

    def on_convert_pressed():
        if window.input_text.toPlainText():
            result = convert(window.input_text.toPlainText())
            window.result.setPlainText(result)
            pyperclip.copy(result)
            window.statusbar.showMessage("Text copied to clipboard")
        else:
            window.statusbar.showMessage("Write something first")
    
    def on_help_pressed():
        window.input_text.setPlainText(example)
        window.result.setPlainText(convert(example))
        window.statusbar.showMessage("App by USBashka")
    
    def on_input_text_edited():
        window.statusbar.showMessage("")
    
    def on_clear_pressed():
        window.input_text.setPlainText("")
        window.result.setPlainText("")
        window.statusbar.showMessage("App by USBashka")
    
    def format(formatter: str):
        itext = window.input_text.toPlainText()
        cursor = window.input_text.textCursor()
        if cursor.hasSelection():
            window.input_text.setPlainText(itext[:cursor.selectionStart()] + formatter +
                itext[cursor.selectionStart():cursor.selectionEnd()] + formatter +
                itext[cursor.selectionEnd():])
        else:
            window.input_text.setPlainText(itext[:cursor.position()] + formatter +
                itext[cursor.position():])
        window.input_text.setTextCursor(cursor)
    
    def on_bold_pressed():
        format("**")
    
    def on_italic_pressed():
        format("*")
    
    def on_mono_pressed():
        format("`")

    # Window creation

    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    window = loader.load(resource_path("ui.ui"), None)
    window.setWindowIcon(QtGui.QIcon(resource_path("icon.bmp")))
    window.input_text.textChanged.connect(on_input_text_edited)
    window.help.clicked.connect(on_help_pressed)
    window.convert.clicked.connect(on_convert_pressed)
    window.clear.clicked.connect(on_clear_pressed)
    window.bold.clicked.connect(on_bold_pressed)
    window.italic.clicked.connect(on_italic_pressed)
    window.mono.clicked.connect(on_mono_pressed)
    window.show()
    window.statusbar.showMessage("App by USBashka")
    app.exec()


if __name__ == "__main__":
    main()
