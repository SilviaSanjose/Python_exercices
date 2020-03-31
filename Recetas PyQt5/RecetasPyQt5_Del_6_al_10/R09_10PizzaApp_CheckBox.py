#Check Box: .stateChanged
import sys
from R09_10Pizza import *
from PyQt5.QtWidgets import QDialog, QApplication


class PreparaPizzas(QDialog):
    def __init__(self):
        super().__init__()
        self.mi_ventana = Ui_Ventana_pizzas()
        self.mi_ventana.setupUi(self)
        
        self.mi_ventana.chk_queso.stateChanged.connect(self.calcular_precio)
        self.mi_ventana.chl_aceitunas.stateChanged.connect(self.calcular_precio)
        self.mi_ventana.chk_salsas.stateChanged.connect(self.calcular_precio)
        
        self.mi_ventana.chk_refresco.stateChanged.connect(self.calcular_precio)
        self.mi_ventana.chk_cerveza.stateChanged.connect(self.calcular_precio)
        
        self.show()
        
    def calcular_precio(self):
        precio_base = 15
        
        if self.mi_ventana.chk_queso.isChecked() == True:
            precio_base += 1
        if self.mi_ventana.chl_aceitunas.isChecked() == True:
            precio_base += 1
        if self.mi_ventana.chk_salsas.isChecked() == True:
            precio_base += 2
        if self.mi_ventana.chk_refresco.isChecked() == True:
            precio_base += 3
        if self.mi_ventana.chk_cerveza.isChecked() == True:
            precio_base += 3
            
        self.mi_ventana.lbl_precio_final.setText("El precio final es {}".format(precio_base))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    abrir_ventana = PreparaPizzas()
    abrir_ventana.show()
    
    sys.exit(app.exec_())
        
        