#Radio Button: .toggled
#Recetas 7 y 8 unidas
import sys
from PyQt5.Qt import QDialog, QApplication
from R07_8EleccionClase import *


class EleccionClaseAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.dialogo = Ui_Dialog()
        self.dialogo.setupUi(self)
        
        self.dialogo.rbtn_primera_clase.toggled.connect(self.mostrar_informacion)
        self.dialogo.rbtn_clase_negocio.toggled.connect(self.mostrar_informacion)
        self.dialogo.rbtn_clase_economica.toggled.connect(self.mostrar_informacion)
        
        self.dialogo.rbtn_tarjeta.toggled.connect(self.mostrar_informacion)
        self.dialogo.rbtn_paypal.toggled.connect(self.mostrar_informacion)
        self.dialogo.rbtn_transferencia.toggled.connect(self.mostrar_informacion)

        self.show()
        
    def mostrar_informacion(self):
        costo_vuelo = 0
        forma_pago = ""
        if self.dialogo.rbtn_primera_clase.isChecked() == True:
            costo_vuelo = 190
        elif self.dialogo.rbtn_clase_negocio.isChecked() == True:
            costo_vuelo = 150
        elif self.dialogo.rbtn_clase_economica.isChecked() == True:
            costo_vuelo = 100
        
        if self.dialogo.rbtn_tarjeta.isChecked()== True:
            forma_pago = "Tarjeta"
        elif self.dialogo.rbtn_paypal.isChecked()== True:
            forma_pago = "Paypal"
        elif self.dialogo.rbtn_transferencia.isChecked()== True:
            forma_pago = "Transferencia Bancaria"
            
        
        self.dialogo.lbl_precio_y_forma_pago.setText("Precio del billete: "+ str(costo_vuelo)+ "€" + " a pagar por " + forma_pago)


    

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = EleccionClaseAplicacion()
    dialogo.show()
    
    sys.exit(app.exec_())