from PyQt5.QtWidgets import QMessageBox


def info_handler(message: str):
    mb1 = QMessageBox()
    mb1.setWindowTitle('Информация')
    mb1.setText(f'{message}')
    mb1.setIcon(QMessageBox.Information)
    mb1.setStandardButtons(QMessageBox.Ok)
    mb1.exec_()
