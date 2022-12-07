#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

list_of_numbers = []


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.setWindowTitle('Работа с массивами и файлами в Python')

        self.btn_upload_data.clicked.connect(self.upload_data_from_file)
        self.btn_process_data.clicked.connect(self.process_data)
        self.btn_save_data.clicked.connect(self.save_data_in_file)
        self.btn_clear.clicked.connect(self.clear)

    def upload_data_from_file(self):
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '',
                                                   "Text Files (*.txt)")[0]

        if path_to_file:
            file = open(path_to_file, 'r')

            data = file.readlines()
            self.plainTextEdit.appendPlainText("Полученные данные: ")
            # выводим считанные данные на экран
            for lines in data:
                self.plainTextEdit.appendPlainText(lines.strip('\n'))

            global list_of_numbers
            list_of_numbers = []

            for lines in data:
                lineSplit = lines.split()
                list_of_numbers.append(lineSplit)

    def process_data(self):
        if validation_of_data():
            sum, max, maxi, maxj, min, mini, minj, sum3 = finder()

            # -*- выполнение задания -*-
            if sum != 0:
                compl(max, maxi, maxj, min, mini, minj, sum3)

                self.plainTextEdit.appendPlainText(
                    "Данные обработаны! " + '\n')

                # выводим список на экран
                for lists in list_of_numbers:
                    for i in lists:
                        new_str = "{:6}".format(str(i))
                        self.plainTextEdit.insertPlainText(new_str)

                    self.plainTextEdit.appendPlainText("")
            else:
                self.plainTextEdit.appendPlainText(
                    "Сумма равна нулю! \n")
        else:
            self.plainTextEdit.appendPlainText("Неправильно введены данные! "
                                               "Таблица должна быть размером "
                                               "5х6 и состоять из чисел! \n")

    def save_data_in_file(self):

        if path_to_file:
            file = open(path_to_file.split(".")[0] + '-Output.txt', 'w')

            for lists in list_of_numbers:
                for i in lists:
                    new_str = "{:6}".format(str(i))
                    file.write(new_str)
                file.write("\n")

            file.close()

            self.plainTextEdit.appendPlainText(
                "Файл был успешно загружен! \n")
        else:
            self.plainTextEdit.appendPlainText("Для начала загрузите файл!")

    def clear(self):
        self.plainTextEdit.clear()


def finder():
    sum = 0
    sum3 = 0
    max = int(list_of_numbers[0][0])
    maxi = 0
    maxj = 0
    min = int(list_of_numbers[0][0])
    mini = 0
    minj = 0

    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers[i])):
            number = int(list_of_numbers[i][j])
            sum += number
            if i == 2:
                sum3 += number
            if max < number:
                max = number
                maxi = i
                maxj = j
            if min > number:
                min = number
                mini = i
                minj = j

    return sum, max, maxi, maxj, min, mini, minj, sum3


def validation_of_data():
    lenth_list = 0
    for lists in list_of_numbers:
        lenth_list += len(lists)
    if lenth_list == 30:
        for lists in list_of_numbers:
            for i in lists:
                try:
                    int(i)
                except Exception:
                    return False
        return True
    else:
        return False


def compl(max, maxi, maxj, min, mini, minj, sum3):
    list_of_numbers[maxi][maxj] = str(max/2)
    list_of_numbers[mini][minj] = str(min - sum3)
    pass


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
