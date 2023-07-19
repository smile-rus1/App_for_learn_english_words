from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QInputDialog

from handlers.information_handler import info_handler
from handlers.negative_handler import negative_handler
from repositories.word import WordRepository
from widjets.words_window import Ui_Words_Window


class WindowWords(QMainWindow):
    def __init__(self, parent=None):
        super(WindowWords, self).__init__(parent)

        self.word_ui = Ui_Words_Window()
        self.word_ui.setupUi(self)

        self.setFixedHeight(395)
        self.setFixedWidth(835)
        self.setWindowTitle("Добавление/Удаление слов")

        self.word_ui.table_words.setColumnWidth(0, 15)
        self.word_ui.table_words.setColumnWidth(1, 200)
        self.word_ui.table_words.setColumnWidth(2, 200)

        self.word_ui.table_words.cellClicked.connect(self.select_row)

        self.word_ui.btn_add_word.clicked.connect(self.add_word)
        self.word_ui.btn_delete_word.clicked.connect(self.delete_word)
        self.word_ui.btn_change_word.clicked.connect(self.update_word_and_translate)

        self.print_all_words()

        self.selected_row = -1

    def select_row(self, row, col):
        self.selected_row = row

    def refresh_table(self):
        self.word_ui.table_words.setRowCount(0)
        self.print_all_words()

    def print_all_words(self):
        lst = WordRepository().get_all()

        self.word_ui.table_words.setRowCount(len(lst))

        for i, row in enumerate(lst):
            tablerow = 0
            self.word_ui.table_words.setItem(i, 0, QTableWidgetItem(str(row[tablerow])))
            tablerow += 1
            self.word_ui.table_words.setItem(i, 1, QTableWidgetItem(str(row[tablerow])))
            tablerow += 1
            self.word_ui.table_words.setItem(i, 2, QTableWidgetItem(str(row[tablerow])))

    def add_word(self):
        try:
            text_words, pressed = QInputDialog.getText(None, 'Введите слово', 'Слово')
            if pressed and text_words != "":

                text_words_tr, pressed_tr = QInputDialog.getText(None, 'Введите перевод', 'Перевод слова')
                if pressed_tr and text_words_tr != "":
                    ...

            if text_words and text_words_tr:
                WordRepository().add_word_and_translate(text_words, text_words_tr)
                self.refresh_table()

        except Exception as ex:
            # negative_handler(f"{ex}")
            negative_handler(f"Возникла ошибка, возможно Вы что-то не так сделали!")

    def delete_word(self):
        try:
            if self.selected_row != -1:
                text_delete = self.word_ui.table_words.item(self.selected_row, 1)

                WordRepository().delete_from_db(text_delete.text())
                self.selected_row = -1
                info_handler(f"Было удалено слово {text_delete.text()}")
                self.refresh_table()

            else:
                text_delete, pressed = QInputDialog.getText(None, 'Введите слово для удаления', 'Слово')
                if pressed and text_delete != "":
                    WordRepository().delete_from_db(text_delete)
                    self.refresh_table()

                    info_handler(f"Было удалено словов {text_delete}")

        except:
            negative_handler("Произошла ошибка, возможно вы не правильно ввели данные!")

    def update_word_and_translate(self):
        data_words = []

        for row in range(self.word_ui.table_words.rowCount()):
            rowdata = []
            for col in range(self.word_ui.table_words.columnCount()):
                rowdata.append(self.word_ui.table_words.item(row, col).data(Qt.EditRole))

            data_words.append(tuple(rowdata))

        for i, dt in enumerate(data_words):
            st = 0
            data = []

            data.append(dt[st])
            st += 1
            data.append(dt[st])
            st += 1
            data.append(dt[st])

            WordRepository().update_words_translate(int(data[0]), data[1], data[2])

        self.refresh_table()
        info_handler("Данные были изменены!")
