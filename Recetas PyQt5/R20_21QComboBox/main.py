import sys
from PyQt5.Qt import QDialog, QApplication
from R20_21QComboBox.lenguajes_programacion import Ui_Lenguajes_programacion_Dialog
from PyQt5 import QtGui

class LenguajeProgramacionApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Lenguajes_programacion_Dialog()
        self.ui.setupUi(self)
        
        self.ui.cbx_lenguajes.currentIndexChanged.connect(self.seleccionar_lenguaje)  #comboBox lenguajes
        
        self.ui.cbx_fuentes.currentFontChanged.connect(self.seleccionar_fuente)      #ComboBox fuentes
        
        self.show()
        
    def seleccionar_lenguaje(self):
        seleccion = self.ui.cbx_lenguajes.itemText(self.ui.cbx_lenguajes.currentIndex())
        self.ui.lbl_eleccion.setText("El lenguaje de programación seleccionado es " + seleccion)
        

    def seleccionar_fuente(self):
        indice = self.ui.cbx_fuentes.currentIndex()       #indice será la fuente actual seleccionada
        fuente_seleccionada = QtGui.QFont(self.ui.cbx_fuentes.itemText(indice), 12)   #puede recibir tamaño de fuente
        self.ui.txt_editor.setFont(fuente_seleccionada)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LenguajeProgramacionApp()
    win.show()
    sys.exit(app.exec_())   