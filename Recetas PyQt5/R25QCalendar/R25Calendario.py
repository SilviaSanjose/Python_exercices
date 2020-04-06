import sys
from PyQt5.Qt import QApplication, QDialog
from R25_26QCalendar.calendar import Ui_Calendar_Dialog
from PyQt5.QtCore import QDate

class Calendario(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Calendar_Dialog()
        self.ui.setupUi(self)
        
        self.ui.cld_calendar.selectionChanged.connect(self.cambiar_fecha)  #al cambiar al fecha en calendario, coencte con funcion

        self.ui.ded_fecha.setDate(QDate.currentDate())    #indico que comience con la fecha actual
    
        self.show()

    
    def cambiar_fecha(self):
        self.ui.ded_fecha.setDate(self.ui.cld_calendar.selectedDate())
    
    
    
    
if __name__== "__main__":
    app = QApplication(sys.argv)
    win = Calendario()
    win.show()
    
    sys.exit(app.exec_())
    