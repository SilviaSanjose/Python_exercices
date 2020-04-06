import sys
from PyQt5.Qt import QApplication, QDialog
from R26QCalendarReservas.reservas import Ui_Reserva_Dialog


class ReservaApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Reserva_Dialog()
        self.ui.setupUi(self)
        
        self.ui.btb_calcular.clicked.connect(self.calcular)
        
        self.show()

    def calcular(self):
        fecha = self.ui.cal_fecha.selectedDate()
        fecha_text = str(fecha.toPyDate())
        
        dias = self.ui.spx_dias.value()
        
        habitacion = self.ui.cbx_habitacion.itemText(self.ui.cbx_habitacion.currentIndex())
        
        self.ui.lbl_seleccion.setText("Fecha: {} - Tipo de Habitación: {} - Nº días: {}".format(fecha_text, habitacion, dias))
        
        precio = 0
        if habitacion =="Individual":
            precio = 20
        elif  habitacion =="Doble":
            precio = 30
        elif habitacion =="Lujo":
            precio = 50
        precio = precio * dias
        
        self.ui.lbl_precio.setText("Precio total: " + str(precio))
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ReservaApp()
    ventana.show()
    sys.exit(app.exec_())