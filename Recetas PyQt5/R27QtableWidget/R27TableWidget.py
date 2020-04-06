import sys
from PyQt5.Qt import QDialog, QApplication, QTableWidgetItem
from R27QtableWidget.tableWidget import Ui_tabla_Dialog

class TablaWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_tabla_Dialog()
        self.ui.setupUi(self)
        
        self.iniciar_datos()
        self.agregar_datos()
    
        self.show()
        
    def iniciar_datos(self):
        self.datos = []
        
        self.datos.append(("Python", "3.8.2"))   
        self.datos.append(("Java", "8")) 
        self.datos.append(("PHP", "7.2")) 
    
    def agregar_datos(self):
        fila = 0
        for registro in self.datos:
            columna = 0
            self.ui.tbl_lenguajes.insertRow(fila)
            for elemento in registro:
                celda = QTableWidgetItem(elemento)
                self.ui.tbl_lenguajes.setItem(fila, columna, celda)
                columna += 1
            fila += 1
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TablaWidget() 
    win.show()
    sys.exit(app.exec_())       