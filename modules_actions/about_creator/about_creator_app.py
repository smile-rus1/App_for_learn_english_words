from PyQt5.QtWidgets import QMessageBox


def message_about_creator_app():
    mb1 = QMessageBox()
    mb1.setWindowTitle('Информация о создателе')
    mb1.setText(f'Данное приложение создал Гасак Руслан Николаевич, учащийся группы ПО-4\n'
                f'Приложение не подразумевает какой-либо коммерческой деятельности и не может быть продано'
                f' или использовано с целью получения прибыли.\n'
                f'Любое копирование или взаимствование запрещено!')
    mb1.setIcon(QMessageBox.Information)
    mb1.setStandardButtons(QMessageBox.Ok)
    mb1.exec_()
