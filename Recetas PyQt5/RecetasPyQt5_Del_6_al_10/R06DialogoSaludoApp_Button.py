#button: .clicked
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from R06DialogoSaludo import Ui_DialogoSaludar

class DialogoSaludoAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        
        self.dialogo = Ui_DialogoSaludar()
        self.dialogo.setupUi(self)
        
        self.dialogo.btn_saludar.clicked.connect(self.mostrar_saludo)
        self.show()
    
    def mostrar_saludo(self):
        mensaje = self.dialogo.txt_nombre.text()     #coge el texto del campo txt_nombre
           #mostrar en el campo lbl_mensaje_saludo lo quie indicamos en setText()
        self.dialogo.lbl_mensaje_saludo.setText("Hola "+ mensaje + "!!!")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = DialogoSaludoAplicacion()
    dialogo.show()
    sys.exit(app.exec_())