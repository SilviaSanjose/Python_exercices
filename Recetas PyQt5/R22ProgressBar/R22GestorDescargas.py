import sys
from PyQt5.Qt import QDialog, QApplication
from R22ProgressBar.gestor_descargas import Ui_Descarga_Dialog



class GestorDescargas(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Descarga_Dialog()
        self.ui.setupUi(self)
        
        self.ui.btn_descarga.clicked.connect(self.iniciar_descarga)
        
        self.show()
        
    def iniciar_descarga(self):
        x = 0
        while x < 100:
            x += 0.00001
            self.ui.pgb_descarga.setValue(x)
        
        


if __name__ =="__main__":
    app = QApplication(sys.argv)
    win = GestorDescargas()
    win.show()
    
    sys.exit(app.exec_())
        