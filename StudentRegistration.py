import sqlite3
import sys
from PySide6.QtWidgets import *

class SchoolFormApp(QMainWindow):
    def __init__(self):
        super(SchoolFormApp, self).__init__()

        self.students = []

        self.setWindowTitle("School Form")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_name = QLabel("Student Name:")
        self.edit_name = QLineEdit()

        self.label_grade = QLabel("Grade:")
        self.edit_grade = QLineEdit()

        self.label_score1 = QLabel("Score 1:")
        self.edit_score1 = QLineEdit()

        self.label_score2 = QLabel("Score 2:")
        self.edit_score2 = QLineEdit()

        self.btn_add = QPushButton("Add")
        self.btn_add.clicked.connect(self.add_student)

        self.btn_delete = QPushButton("Delete Selected")
        self.btn_delete.clicked.connect(self.delete_student)

        self.btn_show = QPushButton("Show Table")
        self.btn_show.clicked.connect(self.show_table)

        self.table_widget = QTableWidget()

        self.layout.addWidget(self.label_name)
        self.layout.addWidget(self.edit_name)
        self.layout.addWidget(self.label_grade)
        self.layout.addWidget(self.edit_grade)
        self.layout.addWidget(self.label_score1)
        self.layout.addWidget(self.edit_score1)
        self.layout.addWidget(self.label_score2)
        self.layout.addWidget(self.edit_score2)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.btn_delete)
        self.layout.addWidget(self.btn_show)
        self.layout.addWidget(self.table_widget)

        self.central_widget.setLayout(self.layout)

    def add_student(self):
        name = self.edit_name.text()
        grade = self.edit_grade.text()
        score1 = float(self.edit_score1.text())
        score2 = float(self.edit_score2.text())
        average = (score1 + score2) / 2

        student = {"Name": name, "Grade": grade, "Score 1": score1, "Score 2": score2, "Average": average}
        self.students.append(student)

        self.edit_name.clear()
        self.edit_grade.clear()
        self.edit_score1.clear()
        self.edit_score2.clear()
        self.show_table()

    def delete_student(self):
        if self.table_widget.currentRow() >= 0:
            selected_row = self.table_widget.currentRow()
            del self.students[selected_row]
            self.show_table()

    def show_table(self):
        self.table_widget.setRowCount(len(self.students))
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Grade", "Score 1", "Score 2", "Average"])

        for row, student in enumerate(self.students):
            for col, (key, value) in enumerate(student.items()):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    school_form_app = SchoolFormApp()
    school_form_app.show()
    sys.exit(app.exec_())
