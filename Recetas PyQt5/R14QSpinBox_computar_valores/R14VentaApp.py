import sys
from R14QSpinBox_computar_valores.venta_dialog import Ui_Dialog
from PyQt5.Qt import QDialog, QApplication

class VentasAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.sbx_cantidad_mouse.editingFinished.connect(self.calcular_total)
        self.ui.sbx_cantidad_teclado.editingFinished.connect(self.calcular_total)
        
        self.show()
        
    def calcular_total(self):
        precio_mouse = int(self.ui.txt_valor_mouse.text())
        cantidad_mouse = int(self.ui.sbx_cantidad_mouse.value())
        total_mouse = precio_mouse * cantidad_mouse
        self.ui.txt_total_mouse.setText(str(total_mouse))
        
        precio_teclado = int(self.ui.txt_valor_teclado.text())
        cantidad_teclaro = int(self.ui.sbx_cantidad_teclado.value())
        total_teclado = precio_teclado * cantidad_teclaro
        self.ui.txt_total_teclado.setText(str(total_teclado))
        
        total = total_mouse + total_teclado
        self.ui.lbl_total.setText("Total a pagar: " + str(total))
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = VentasAplicacion()
    dialog.show()
    
    sys.exit(app.exec_())