from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from repositories.learn_word import LearnRepository
from widjets.learn_words_window import Ui_Learn_Words_Window


class WindowLearn(QMainWindow):
    def __init__(self, parent=None):
        super(WindowLearn, self).__init__(parent)

        self.learn_ui = Ui_Learn_Words_Window()
        self.learn_ui.setupUi(self)

        self.setFixedHeight(435)
        self.setFixedWidth(800)
        self.setWindowTitle("Окно для слов")

        self.learn_ui.table_words.setColumnWidth(0, 200)
        self.learn_ui.table_words.setColumnWidth(1, 200)

        self.learn_ui.btn_output_in_order.clicked.connect(self.out_in_order)
        self.learn_ui.btn_output_in_diffrent.clicked.connect(self.out_in_random)

    def out_in_order(self):
        lst = LearnRepository().out_total_words(self.learn_ui.spinBox.value())
        self.learn_ui.table_words.setRowCount(len(lst))

        for i, row in enumerate(lst):
            tablerow = 0
            self.learn_ui.table_words.setItem(i, 0, QTableWidgetItem(str(row[tablerow])))
            tablerow += 1
            self.learn_ui.table_words.setItem(i, 1, QTableWidgetItem(str(row[tablerow])))

    def out_in_random(self):
        lst = LearnRepository().out_random_choice_words(self.learn_ui.spinBox.value())
        self.learn_ui.table_words.setRowCount(len(lst))

        for i, row in enumerate(lst):
            tablerow = 0
            self.learn_ui.table_words.setItem(i, 0, QTableWidgetItem(str(row[tablerow])))
            tablerow += 1
            self.learn_ui.table_words.setItem(i, 1, QTableWidgetItem(str(row[tablerow])))
