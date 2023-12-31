from PyQt5.QtWidgets import QMessageBox


def message_about_add_delete_words():
    mb1 = QMessageBox()
    mb1.setWindowTitle('Информация о вкладке "Слова "Добавить/Удалить""')
    mb1.setText(f"В даной вкладке Вы можете добавить/удалить/изменить перевод слов\n"
                f"Для того чтобы добавить слово нужно нажать на кнопку 'Добавить слово' после чего вам нужно будет "
                f"ввести само слово и его перевод\n"
                f"Для того чтобы удалить слово:\n"
                f"1. Нажать на кнопку 'Удалить слово' и ввести слово, которое вы хотите удалить\n"
                f"2. Выделить из таблицы слово, которое хотите удалить и нажать на кнопку 'Удалить слово'\n"
                f"Для того чтобы изменить перевод или слово, в таблице измените какое вам надо слово/слова или их "
                f"перевод и нажмите на кнопку 'Изменить слово/перевод'")
    mb1.setIcon(QMessageBox.Information)
    mb1.setStandardButtons(QMessageBox.Ok)
    mb1.exec_()
