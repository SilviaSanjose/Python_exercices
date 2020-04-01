import sys
from R13Calculadora.Calculadora import Ui_calculadora
from PyQt5.Qt import QApplication, QDialog

class Calculadora(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_calculadora()
        self.ui.setupUi(self)
        
        self.ui.btn_suma.clicked.connect(self.sumar)
        self.ui.btn_resta.clicked.connect(self.restar)
        self.ui.btn_multiplicar.clicked.connect(self.multiplicar)
        self.ui.btn_division.clicked.connect(self.dividir)
      
        self.show()
        
    def sumar(self):
        numeroUno = 0
        numeroDos = 0
    
        if len(self.ui.txt_primer_numero.text()) > 0:
            numeroUno = float(self.ui.txt_primer_numero.text())
            
        if len(self.ui.txt_segundo_numero.text()) > 0:
            numeroDos = float(self.ui.txt_segundo_numero.text())
             
        suma = numeroUno + numeroDos
        
        self.ui.lbl_resultado.setText("Resultado: " + str(suma))
    def restar(self):
        numeroUno = 0
        numeroDos = 0
        
        if len(self.ui.txt_primer_numero.text()) > 0:
            numeroUno = float(self.ui.txt_primer_numero.text())
        if len(self.ui.txt_segundo_numero.text()) > 0:
            numeroDos = float(self.ui.txt_segundo_numero.text())  
             
        resta = numeroUno - numeroDos
        
        self.ui.lbl_resultado.setText("Resultado: " + str(resta))
        
    def multiplicar(self):
        numeroUno = 0
        numeroDos = 0
        
        if len(self.ui.txt_primer_numero.text()) > 0:
            numeroUno = float(self.ui.txt_primer_numero.text())
        if len(self.ui.txt_segundo_numero.text()) > 0:
            numeroDos = float(self.ui.txt_segundo_numero.text())
               
        multiplicacion = numeroUno * numeroDos
        
        self.ui.lbl_resultado.setText("Resultado: " + str(multiplicacion))
        
    def dividir(self):
        numeroUno = 0
        numeroDos = 0
        
        if len(self.ui.txt_primer_numero.text()) > 0:
            numeroUno = float(self.ui.txt_primer_numero.text())
        if len(self.ui.txt_segundo_numero.text()) > 0:
            numeroDos = float(self.ui.txt_segundo_numero.text())   
        division = numeroUno / numeroDos
        
        self.ui.lbl_resultado.setText("Resultado: " + str(division))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    
    sys.exit(app.exec_())
    