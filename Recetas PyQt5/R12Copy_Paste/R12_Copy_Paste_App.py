import sys
from R12Copy_Paste.Copy_Paste import Ui_CopiaryPegar
from PyQt5.Qt import QDialog, QApplication


class CopiarPegar(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CopiaryPegar()
        self.ui.setupUi(self)
        
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    venta = CopiarPegar()
    venta.show()
    
    sys.exit(app.exec_())

'''En designer; Edit/Edit Signal/Events >> modificamos que pasa al pulsar el botón.
Como es necesario seleccionar lo que escriba y copiarlo, en vez del evento click()
indicamos:
Botón copiar: Cuando presionemos > pressed() >> selectAll()   Con esto selecciona todo del campo text que indicamos
              Cuando soltamos > realased() >> copy()       Copiamos el texto seleccionado.
Botón pegar: Cuando hacemos click() >> paste()   Pegamos en el campo text, de destino que indicamos. 
'''    