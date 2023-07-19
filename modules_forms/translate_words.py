import random

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QInputDialog

from handlers.information_handler import info_handler
from handlers.negative_handler import negative_handler
from repositories.translate_word import TranslateRepository
from widjets.translate_words_window import Ui_Translate_Window


class TranslateWindow(QMainWindow):
    def __init__(self, parent=None):
        super(TranslateWindow, self).__init__(parent)

        self.sec = 0
        self.answer = ""
        self.translate = ""
        self.list_of_words = []
        self.flag = True
        self.count_right_answer = 0
        self.count_total = 0

        self.translate_ui = Ui_Translate_Window()
        self.translate_ui.setupUi(self)

        self.setFixedHeight(505)
        self.setFixedWidth(800)
        self.setWindowTitle("Перевод слов")

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.translate_ui.btn_accept.setEnabled(False)
        self.translate_ui.btn_skip_word.setEnabled(False)

        self.translate_ui.btn_start_end.clicked.connect(self.on_start)
        self.translate_ui.btn_skip_word.clicked.connect(self.skip_word)
        self.translate_ui.btn_accept.clicked.connect(self.on_right_write)

    def update_timer(self):
        self.sec += 1
        self.translate_ui.timer_label.setText(str(self.sec))

    def on_start(self):
        if self.translate_ui.radio_basic.isChecked():
            self.change_text_in_btn()
            self.check_state()

        if self.translate_ui.radio_faster.isChecked():
            self.toggle_timer()
            self.change_text_in_btn()
            self.check_state()

        if self.translate_ui.radio_on_total.isChecked():
            if not self.list_of_words and self.flag:
                self.output_definite_number_words_list()
                self.flag = False

            self.change_text_in_btn()
            self.check_state()

    def change_text_in_btn(self):
        if self.translate_ui.btn_start_end.text() == "Начать":
            self.translate_ui.btn_start_end.setText("Остановить")
            self.write_word_on_edt()

        elif self.translate_ui.btn_start_end.text() == "Остановить":
            self.translate_ui.btn_start_end.setText("Начать")
            self.list_of_words = []
            self.flag = True

    def toggle_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)

        else:
            self.timer.stop()
            self.sec = 0
            self.translate_ui.timer_label.setText("0")

    def get_word(self):
        """
        будет возвращать случайное слово из бд
        :yield:
        """
        gen = TranslateRepository().get_one_word()
        word = next(gen)

        self.answer = word[0]

    def get_translate_to_word(self) -> None:
        """
        в переменную ложит перевод слова
        :return:
        """
        gen = TranslateRepository().output_translate_word(self.answer)
        translate = next(gen)
        self.translate = translate

    def skip_word(self) -> None:
        self.write_word_on_edt()
        if self.count_total != 0 and self.translate_ui.radio_on_total.isChecked():
            return
        self.count_total += 1

    def write_word_on_edt(self) -> None:
        if not self.translate_ui.radio_on_total.isChecked():
            self.get_word()
        else:
            if not self.list_of_words:
                self.change_text_in_btn()
                self.check_state()
                return

            self.answer = self.list_of_words.pop()

        self.translate_ui.edit_to_out.setText(self.answer)

    def on_right_write(self):
        self.get_translate_to_word()

        if self.translate == self.translate_ui.edit_to_input.text():
            self.count_right_answer += 1

        self.write_word_on_edt()
        self.translate_ui.edit_to_input.setText("")
        if self.count_total != 0 and self.translate_ui.radio_on_total.isChecked():
            return

        self.count_total += 1

    def output_definite_number_words_list(self) -> None:
        try:
            quantity_words, pressed = QInputDialog.getInt(None, 'Введите количество слов, которое нужно вывести',
                                                          "Количество")
            if pressed and quantity_words != "":
                if quantity_words <= 0:
                    raise ValueError

            gen = TranslateRepository().get_count_words(quantity_words)
            words = next(gen)

            self.list_of_words = [word[0] for word in words]
            if quantity_words > len(self.list_of_words):
                self.count_total = len(self.list_of_words)
            else:
                self.count_total = quantity_words

        except ValueError:
            negative_handler("Количество слов не может быть меньше или равно 0!")

        except Exception:
            negative_handler("Произошла ошибка, возможно вы не правильно ввели данные!")

    def check_state(self):
        if self.translate_ui.btn_start_end.text() == "Остановить":
            self.translate_ui.edit_to_input.setReadOnly(False)

            if self.translate_ui.radio_basic.isChecked():
                self.translate_ui.radio_faster.setCheckable(False)
                self.translate_ui.radio_on_total.setCheckable(False)

            if self.translate_ui.radio_faster.isChecked():
                self.translate_ui.radio_basic.setCheckable(False)
                self.translate_ui.radio_on_total.setCheckable(False)

            if self.translate_ui.radio_on_total.isChecked():
                self.translate_ui.radio_basic.setCheckable(False)
                self.translate_ui.radio_faster.setCheckable(False)

            self.translate_ui.btn_accept.setEnabled(True)
            self.translate_ui.btn_skip_word.setEnabled(True)

        else:
            self.translate_ui.edit_to_input.setReadOnly(True)
            self.translate_ui.edit_to_input.setText("")
            self.translate_ui.edit_to_out.setText("")
            self.translate_ui.radio_basic.setCheckable(True)
            self.translate_ui.radio_faster.setCheckable(True)
            self.translate_ui.radio_on_total.setCheckable(True)
            self.translate_ui.btn_accept.setEnabled(False)
            self.translate_ui.btn_skip_word.setEnabled(False)

            info_handler(f"Количество правильных ответов {self.count_right_answer} из {self.count_total}")
            self.count_right_answer = 0
            self.count_total = 0
