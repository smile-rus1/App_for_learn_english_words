from PyQt5.QtWidgets import QMainWindow, QInputDialog

from handlers.information_handler import info_handler
from handlers.negative_handler import negative_handler
from repositories.correct_word import CorrectRepository
from widjets.correct_write_window import Ui_CorrectWrite_Window


class WindowCorrectWrite(QMainWindow):
    def __init__(self, parent=None):
        super(WindowCorrectWrite, self).__init__(parent)

        self.correct_ui = Ui_CorrectWrite_Window()
        self.correct_ui.setupUi(self)

        self.setFixedHeight(435)
        self.setFixedWidth(800)
        self.setWindowTitle("Окно для правильного написания слов")

        self.translate = ""
        self.word = ""
        self.count_right_answer = 0
        self.count_total = 0
        self.list_of_words = []

        self.correct_ui.btn_accept.setEnabled(False)
        self.correct_ui.btn_skip_word.setEnabled(False)

        self.correct_ui.btn_start_end.clicked.connect(self.on_start)
        self.correct_ui.btn_accept.clicked.connect(self.right_write)
        self.correct_ui.btn_skip_word.clicked.connect(self.skip_word)

    def on_start(self):
        self.change_text_in_btn()
        self.check_state()

    def change_text_in_btn(self):
        if self.correct_ui.btn_start_end.text() == "Начать":
            self.correct_ui.btn_start_end.setText("Остановить")

            if self.correct_ui.radio_basic.isChecked():
                self.simple_mode()

            if self.correct_ui.radio_on_total.isChecked():
                self.get_quantity_translate_words()
                self.output_quantity_words()
                print(self.list_of_words)

        elif self.correct_ui.btn_start_end.text() == "Остановить":
            self.correct_ui.btn_start_end.setText("Начать")

    def check_state(self):
        if self.correct_ui.btn_start_end.text() == "Остановить":
            self.correct_ui.edit_to_input.setReadOnly(False)

            if self.correct_ui.radio_basic.isChecked():
                self.correct_ui.radio_on_total.setCheckable(False)

            if self.correct_ui.radio_on_total.isChecked():
                self.correct_ui.radio_basic.setCheckable(False)

            self.correct_ui.btn_accept.setEnabled(True)
            self.correct_ui.btn_skip_word.setEnabled(True)

        else:
            self.correct_ui.edit_to_input.setReadOnly(True)
            self.correct_ui.edit_to_input.setText("")
            self.correct_ui.edit_to_out.setText("")
            self.correct_ui.radio_basic.setCheckable(True)
            self.correct_ui.radio_on_total.setCheckable(True)
            self.correct_ui.btn_accept.setEnabled(False)
            self.correct_ui.btn_skip_word.setEnabled(False)

            info_handler(f"Количество правильных ответов {self.count_right_answer} из {self.count_total}")
            self.count_right_answer = 0
            self.count_total = 0

    def get_one_translate(self):
        if self.correct_ui.radio_basic.isChecked():
            gen = CorrectRepository().get_translate_word()
            self.translate = next(gen)[0]

    def get_word(self):
        gen = CorrectRepository().output_word(self.translate)
        self.word = next(gen)

    def right_write(self):
        self.get_word()
        if self.word == self.correct_ui.edit_to_input.text():
            self.count_right_answer += 1

        self.correct_ui.edit_to_input.setText("")

        if self.correct_ui.radio_on_total.isChecked():
            self.output_quantity_words()
            return

        self.count_total += 1

    def simple_mode(self):
        self.get_one_translate()
        self.correct_ui.edit_to_out.setText(self.translate)

    def get_quantity_translate_words(self):
        try:
            quantity_words, pressed = QInputDialog.getInt(None, 'Введите количество слов, которое нужно вывести',
                                                          "Количество")
            if pressed and quantity_words != "":
                if quantity_words <= 0:
                    raise ValueError

            gen = CorrectRepository().get_quantity_translates_words(quantity_words)
            translates = next(gen)
            self.list_of_words = [translate[0] for translate in translates]
            if quantity_words > len(self.list_of_words):
                self.count_total = len(self.list_of_words)
            else:
                self.count_total = quantity_words

        except ValueError:
            negative_handler("Количество слов не может быть меньше 0!")

        except:
            negative_handler("Произошла ошибка, возможно вы не правильно ввели данные!")

    def output_quantity_words(self):
        if self.list_of_words:
            self.translate = self.list_of_words.pop()
            self.correct_ui.edit_to_out.setText(self.translate)
        else:
            self.change_text_in_btn()
            self.check_state()

    def skip_word(self):
        if self.correct_ui.radio_basic.isChecked():
            self.simple_mode()
            self.count_total += 1

        if self.correct_ui.radio_on_total.isChecked():
            self.output_quantity_words()
