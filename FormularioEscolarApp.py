import sqlite3
import sys
from PySide6.QtWidgets import *

class FormularioEscolarApp(QMainWindow):
    def __init__(self):
        super(FormularioEscolarApp, self).__init__() 

        self.alunos = []

        self.setWindowTitle("Formulário Escolar") 
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget) 

        self.layout = QVBoxLayout() 

        self.label_nome = QLabel("Nome do Aluno:")
        self.edit_nome = QLineEdit()

        self.label_serie = QLabel("Série:")
        self.edit_serie = QLineEdit()

        self.label_nota1 = QLabel("Nota 1:")
        self.edit_nota1 = QLineEdit()

        self.label_nota2 = QLabel("Nota 2:")
        self.edit_nota2 = QLineEdit()

        self.btn_adicionar = QPushButton("Adicionar") 
        self.btn_adicionar.clicked.connect(self.adicionar_aluno) 

        self.btn_deletar = QPushButton("Deletar Selecionado")
        self.btn_deletar.clicked.connect(self.deletar_aluno)

        self.btn_mostrar = QPushButton("Mostrar Tabela")
        self.btn_mostrar.clicked.connect(self.mostrar_tabela)

        self.table_widget = QTableWidget() 

        self.layout.addWidget(self.label_nome) 
        self.layout.addWidget(self.edit_nome)
        self.layout.addWidget(self.label_serie)
        self.layout.addWidget(self.edit_serie)
        self.layout.addWidget(self.label_nota1)
        self.layout.addWidget(self.edit_nota1)
        self.layout.addWidget(self.label_nota2)
        self.layout.addWidget(self.edit_nota2)
        self.layout.addWidget(self.btn_adicionar)
        self.layout.addWidget(self.btn_deletar)
        self.layout.addWidget(self.btn_mostrar)
        self.layout.addWidget(self.table_widget)

        self.central_widget.setLayout(self.layout) 

    def adicionar_aluno(self): 
        nome = self.edit_nome.text()
        serie = self.edit_serie.text()
        nota1 = float(self.edit_nota1.text())
        nota2 = float(self.edit_nota2.text())
        media = (nota1 + nota2) / 2

        aluno = {"Nome": nome, "Série": serie, "Nota 1": nota1, "Nota 2": nota2, "Média": media}
        self.alunos.append(aluno)

        self.edit_nome.clear() 
        self.edit_serie.clear()
        self.edit_nota1.clear()
        self.edit_nota2.clear()
        self.mostrar_tabela()

    def deletar_aluno(self):
        
        if self.table_widget.currentRow() >= 0:
            
            selected_row = self.table_widget.currentRow()

           
            del self.alunos[selected_row]

            
            self.mostrar_tabela()

    def mostrar_tabela(self): 
        self.table_widget.setRowCount(len(self.alunos)) 
        self.table_widget.setColumnCount(5) 
        self.table_widget.setHorizontalHeaderLabels(["Nome", "Série", "Nota 1", "Nota 2", "Média"]) 

        for row, aluno in enumerate(self.alunos): 
            for col, (key, value) in enumerate(aluno.items()): 
                item = QTableWidgetItem(str(value)) 
                self.table_widget.setItem(row, col, item) 


if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    formulario_app = FormularioEscolarApp()
    formulario_app.show() 
    sys.exit(app.exec_()) 
