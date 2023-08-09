import os
import sys

from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox
from PySide6.QtCore import Qt
from convert_ui import Ui_Form


class Window(QWidget, Ui_Form):
    def __init__(self):
        super(Window, self).__init__()
        self.label_path = None
        self.new_data = []

        self.setupUi(self)
        self.pushButton_openpath.clicked.connect(self.open_path)
        self.pushButton_start.clicked.connect(self.start)

    def open_path(self):
        self.label_path = QFileDialog.getExistingDirectory(self, 'Open Folder', './')
        self.textEdit_path.setText(self.label_path)
        # if self.label_path != '':
        #     print('filename:', self.label_path)

    def start(self):
        if self.radioButton_delete.isChecked():
            mb = QMessageBox.question(self, 'Sure?',
                                      f'Is it correct you chose to delete class "{self.spinBox_deleteclass.value()}" '
                                      f'of label files in {self.label_path}?')
            if mb == QMessageBox.StandardButton.Yes:
                self.delete()

        elif self.radioButton_edit.isChecked():
            mb = QMessageBox.question(self, 'Sure?',
                                      f'Is it correct you chose to change class "{self.spinBox_editfrom.value()}" '
                                      f'to "{self.spinBox_editto.value()}" of label files in {self.label_path}?')
            if mb == QMessageBox.StandardButton.Yes:
                self.edit()

    def delete(self):
        self.new_data = []
        label_list = os.listdir(self.label_path)
        for i in label_list:
            with open(f'{self.label_path}/{i}', 'r') as fr:
                data = fr.readlines()
                for value in data:
                    if value[:1] != f'{self.spinBox_editfrom.value()}':
                        value = f'{self.spinBox_editto.value()}' + value[1:]
                    self.new_data.append(value)

            # with open(f'{self.label_path}/{i}', 'w') as fw:
            #     fw.writelines(self.new_data)
        print(self.new_data)
        QMessageBox.information(self, 'Complete', 'The delete is completed.')

    def edit(self):
        self.new_data = []
        label_list = os.listdir(self.label_path)
        for i in label_list:
            with open(f'{self.label_path}/{i}', 'r') as fr:
                data = fr.readlines()
                for value in data:
                    if value[:1] == f'{self.spinBox_editfrom.value()}':
                        value = f'{self.spinBox_editto.value()}' + value[1:]
                    self.new_data.append(value)

            # with open(f'{self.label_path}/{i}', 'w') as fw:
            #     fw.writelines(self.new_data)
            # break

        print(self.new_data)
        QMessageBox.information(self, 'Complete', 'The change is completed.')

    def keyPressEvent(self, event: QKeyEvent):
        if event.modifiers() & Qt.ControlModifier:
            if event.key() == Qt.Key_W:
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
