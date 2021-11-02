class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self.canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self.control = None
        self._numTV += 1
    
    def setMarca(self, marca):
        self._marca = marca
    
    def getMarca(self):
        return self._marca
    
    def setControl(self, control):
        self.control = control
    
    def getControl(self):
        return self.control

    def setPrecio(self, precio):
        self._precio = precio
    
    def getPrecio(self):
        return self._precio
    
    def setVolumen(self, vol):
        self._volumen = vol
    
    def getVolumen(self):
        return self._volumen
    
    def setCanal(self, can):
        if self._estado == True and 1 <= can <= 120:
            self.canal = can

    def getCanal(self):
        return self.canal

    def getnumTV(self):
        return self._numTV
    
    def turnOn(self):
        if self._estado == False:
            self._estado = True
    
    def turnOff(self):
        if self._estado == True:
            self._estado = False
    
    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if self._estado == True and 1 <= self.canal < 120:
            self.canal += 1
    
    def canalDown(self):
        if self._estado == True and 1 < self.canal <= 120:
            self.canal -= 1
    
    def volumenUp(self):
        if self._estado == True and 0 <= self._volumen < 7:
            self._volumen += 1
    def volumenDown(self):
        if self._estado == True and 0 < self._volumen <= 7:
            self._volumen -= 1