from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QGridLayout, QWidget, QLineEdit
import sys
from functools import partial
from PySide6.QtCore import Qt
import os
os.system("cls")

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setFixedSize(255,255)
        self.General = QWidget()
        self.setCentralWidget(self.General)
        
        self.layout_principal = QVBoxLayout()
        self.General.setLayout(self.layout_principal)
        
        self._crear_area()
        self._botones()
        # Señalas
        self._conectar_botones()
        
    def _crear_area(self):
        self.contenedor = QLineEdit()
        self.contenedor.setFixedHeight(35)
        self.contenedor.setAlignment(Qt.AlignRight)
        self.contenedor.setReadOnly(True)
        self.layout_principal.addWidget(self.contenedor)        
        
        
    def _botones(self):
        # Dictionary
        self.botones = {}
        layout_botones = QGridLayout()
        self.botones = {
            '7': (0,0),
            '8': (0,1),
            '9': (0,2),
            '/': (0,3),
            '4': (1,0),
            '5': (1,1),
            '6': (1,2), 
            '*': (1,3),
            '1': (2,0),
            '2': (2,1),
            '3': (2,2),
            '-': (2,3),
            '0': (3,0),
            '.': (3,1),
            'C': (3,2),
            '+': (3,3),
            '=': (3,4)           
        }
        
        for texto_boton, position in self.botones.items():
            self.botones[texto_boton] = QPushButton(texto_boton) 
            self.botones[texto_boton].setFixedSize(40,40)   
            # Publicamos
            layout_botones.addWidget(self.botones[texto_boton], position[0], position[1])
        
            self.layout_principal.addLayout(layout_botones)
   
    def _conectar_botones(self):
        
        for texto_boton, boton in self.botones.items():
            if texto_boton not in {'=', 'C'}:
                boton.clicked.connect(partial(self._construir_expresion, texto_boton))
    
        # Limpiar 
        self.botones['C'].clicked.connect(self._limpiar_entrada) 
        self.botones['='].clicked.connect(self._calcular_resultado)
        self.contenedor.returnPressed.connect(self._calcular_resultado)   
    
    def _construir_expresion(self, texto_boton):
        expresion = self.obtener_texto() + texto_boton
        self.actualizar_texto(expresion)
        
    def obtener_texto(self):
        return self.contenedor.text()         
    
    def actualizar_texto(self, texto):
        self.contenedor.setText(texto)
        self.contenedor.setFocus()
    
    def _limpiar_entrada(self):
        self.actualizar_texto('') 
        
    def _calcular_resultado(self):
        resultado = self._evaluar_expresion(self.obtener_texto())   
        self.actualizar_texto(resultado)
    
    def _evaluar_expresion(self, expresion):
        try:
            resultado = str(eval(expresion))
        
        except Exception as e:
            resultado = 'Ocurrio un error' 
        
        return resultado            
               
if __name__ == '__main__':
    app = QApplication([])
    venv = Calculator()
    venv.show()
    
    sys.exit(app.exec())        