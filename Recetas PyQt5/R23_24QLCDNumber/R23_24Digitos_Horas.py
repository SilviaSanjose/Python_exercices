import sys
from PyQt5.Qt import QDialog, QLCDNumber, QApplication, QTime, QTimer
from R23_24QLCDNumber.visor_number import Ui_Dialog
#from PyQt5.QtCore import QTime


class Visor_Numeros(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
    #CONVERSION NUMEROS
        #indico que convierta el nº que indica el usuario en el txt
        self.ui.lcdNumber.display(self.ui.txt_introduccion.text())
        self.ui.lcdNumber.setDigitCount(9)  #dígitos para incluir
        #indica que cuando cambie el texto, recoga ese valor en el lcd
        self.ui.txt_introduccion.textChanged.connect(self.ui.lcdNumber.display)
        
        self.ui.btn_decimal.clicked.connect(self.cambiar_decimal)
        self.ui.btn_binario.clicked.connect(self.cambiar_binario)
        self.ui.btn_octal.clicked.connect(self.cambiar_octal)
        self.ui.btn_hexa.clicked.connect(self.cambiar_hexadecimal)
        
    #MOSTRAR HORA
        timer = QTimer(self)
        timer.timeout.connect(self.tick)   #TICK indica cada cambio de tiempo 
        timer.start(1000)    #intervalor de cambio de tiempo 1000 milisengundo = 1 seg
        
        self.tick()
        
        self.show()
        
    def cambiar_decimal(self):
        self.ui.lcdNumber.setMode(QLCDNumber.Dec)
        
    def cambiar_binario(self):
        self.ui.lcdNumber.setMode(QLCDNumber.Bin)
    
    def cambiar_octal(self):
        self.ui.lcdNumber.setMode(QLCDNumber.Oct)
        
    def cambiar_hexadecimal(self):
        self.ui.lcdNumber.setMode(QLCDNumber.Hex)
    
    
    def tick(self):   
        hora = QTime.currentTime()
        hora_txt = hora.toString("hh:mm")
        
        self.ui.lcd_hora.display(hora_txt)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Visor_Numeros()
    win.show()
    
    sys.exit(app.exec_())