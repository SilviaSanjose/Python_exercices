import sys
from R15QSlider.Niveles_salud import Ui_Niveles_Dialog
from PyQt5.Qt import QDialog, QApplication

class NivelesSalud(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Niveles_Dialog()
        self.ui.setupUi(self)
        
        self.ui.hsb_nivel_azucar.valueChanged.connect(self.mostrar_azucar)
        self.ui.hsd_presion_arterial.valueChanged.connect(self.mostrar_presion_arterial)
        self.ui.vsb_pulso.valueChanged.connect(self.mostrar_pulso)
        self.ui.vsd_colesterol.valueChanged.connect(self.mostrar_colesterol)
        
        self.show()
        
    def mostrar_azucar(self, valor):
        self.ui.txt_resultado_azucar.setText("Nivel azucar: " + str(valor))
    
    def mostrar_presion_arterial(self, valor):
        self.ui.txt_resultado_pArterial.setText("Presión Arterial: {}".format(valor))
        
    def mostrar_pulso(self, valor):
        self.ui.txt_resultado_pulso.setText("Pulso: {}".format(valor))
        
    def mostrar_colesterol(self, valor):
        self.ui.txt_resultado_colesterol.setText("Colesterol: {}".format(valor))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = NivelesSalud()
    dialog.show()
    
    sys.exit(app.exec_())        
    