from PyQt5.QtWidgets import QDockWidget,QSpinBox,QPushButton,QFormLayout,QWidget

class Actions(QDockWidget):
    #creamos todos los botones y spinbox necesarios en el programa
    def __init__(self,parent=None):
        super(Actions,self).__init__(parent)

        self.__mapsize__=QSpinBox()
        self.__animals__=QSpinBox()
        self.__cycles__=QSpinBox()
        self.__new_entitys__=QSpinBox()
        
        self.reset=QPushButton('Reiniciar juego')
        self.newcycles=QPushButton('Ejecutar Rondas')
        self.new_entitys_panda=QPushButton('Crear pandas')
        self.new_entitys_bambu=QPushButton('Crear bambu')
        self.actualizar=QPushButton('Actualizar mapa')

        layout=QFormLayout()
        layout.addRow('Tamaño del mapa',self.__mapsize__)
        layout.addRow('Entidades',self.__animals__)
        layout.addRow(self.reset)
        
        layout.addRow('Rondas',self.__cycles__)
        layout.addRow(self.newcycles)
        
        layout.addRow('Entidades: ',self.__new_entitys__)
        layout.addRow(self.new_entitys_panda)
        layout.addRow(self.new_entitys_bambu)
        
        layout.addRow(self.actualizar)

        main =QWidget()
        main.setLayout(layout)
        self.setWidget(main)
