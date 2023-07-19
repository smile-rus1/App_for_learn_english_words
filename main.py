import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from data_base.create_db import create_db

from modules_actions.about_app.about_learn_words import message_about_learn_words
from modules_actions.about_app.about_right_wrote_words import message_about_correct_wrote_words
from modules_actions.about_app.about_translate_words import message_about_translate_words
from modules_actions.about_creator.about_creator_app import message_about_creator_app
from modules_actions.about_words.about_add_delete_words import message_about_add_delete_words

from modules_actions.words import WindowWords
from modules_forms.correct_write_words import WindowCorrectWrite

from modules_forms.learn_words import WindowLearn
from modules_forms.translate_words import TranslateWindow

from widjets.main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        self.main_ui.for_learn_words.triggered.connect(lambda: message_about_learn_words())
        self.main_ui.for_translate_words.triggered.connect(lambda: message_about_translate_words())
        self.main_ui.for_correct_words.triggered.connect(lambda: message_about_correct_wrote_words())
        self.main_ui.info_about_add_delete.triggered.connect(lambda: message_about_add_delete_words())

        self.main_ui.for_creator_app.triggered.connect(lambda: message_about_creator_app())

        self.main_ui.action_words.triggered.connect(lambda: WindowWords(self).show())

        self.main_ui.btn_open_learn_words.clicked.connect(lambda: WindowLearn(self).show())
        self.main_ui.btn_open_translate_words.clicked.connect(lambda: TranslateWindow(self).show())
        self.main_ui.btn_open_currect_words.clicked.connect(lambda: WindowCorrectWrite(self).show())

        create_db()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedHeight(295)
    widget.setFixedWidth(650)
    widget.setWindowTitle("Главное меню")
    widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
