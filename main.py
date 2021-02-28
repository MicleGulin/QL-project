# Импорт библиотек
import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog


# from add_student import Ui_Dialog_add_student


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/main.ui', self)

        # По умолчанию будем выводить все данные из таблицы
        self.show_data()
        self.pushButton_Run.clicked.connect(self.show_data)

        # Добавление нового ученика
        self.pushButton_add_student.clicked.connect(self.add_student)

        # Удаление нового ученика
        self.pushButton_del_student.clicked.connect(self.del_student)

        # Настройки


    def show_table(self, name, tableWidget_name, col):
        cur = self.connection.cursor()
        cur.execute(f'SELECT * FROM {name}')
        rows = cur.fetchall()
        eval(tableWidget_name).setColumnCount(col)
        eval(tableWidget_name).setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(rows):
            eval(tableWidget_name).setRowCount(
                eval(tableWidget_name).rowCount() + 1)
            for j, elem in enumerate(row):
                eval(tableWidget_name).setItem(i, j, QTableWidgetItem(str(elem)))
        # self.connection.close()

    def show_data(self):
        self.connection = sqlite3.connect("data/movement of people.db")
        self.show_table('students', 'self.tableWidget_students', 6)
        self.show_table('parents', 'self.tableWidget_parents', 5)
        self.show_table('movements', 'self.tableWidget_movements', 5)
        self.connection.close()

    # def closeEvent(self, event):
    #     # При закрытии формы закроем и наше соединение
    #     # с базой данных
    #     self.connection.close()

    def add_student(self):
        self.ex1 = Dialog_Add_Student()
        self.ex1.show()

    def  del_student(self):
        pass


class Dialog_Add_Student(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/add_student.ui', self)

    def accept(self):
        # Запись данных нового ученика

        self.connection = sqlite3.connect("data/movement of people.db")
        cur1 = self.connection.cursor()
        print(self.lineEdit_id_students.text())
        print(self.lineEdit_stud_family.text())
        print(self.lineEdit_stud_name.text())
        print(self.lineEdit_stud_sec_name.text())
        print(self.lineEdit_stud_class.text())
        print(self.lineEdit_id_parents.text())
        # x = cur1.execute('INSERT INTO students VALUES("1", "2", "3", "4", "5", "6")')

        cur1.execute(
            f'''INSERT INTO students VALUES ({self.lineEdit_id_students.text()}, 
             {self.lineEdit_stud_family.text()}, {self.lineEdit_stud_name.text()}, 
             {self.lineEdit_stud_sec_name.text()}, {self.lineEdit_stud_class.text()}, 
             {self.lineEdit_id_parents.text()})''')
        self.connection.commit()
        self.connection.close()

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = Main_Window()
ex.show()
sys.exit(app.exec())
