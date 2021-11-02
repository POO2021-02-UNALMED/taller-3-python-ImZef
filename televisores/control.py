from televisores.tv import TV

class Control:
    def __init__(self):
        self._tv = None
    
    def turnOn(self):
        self._tv.turnOn()
    
    def turnOff(self):
        self._tv.turnOff()
    
    def canalUp(self):
        self._tv.canalUp()
    
    def canalDowm(self):
        self._tv.canalDown()
    
    def volumenDown(self):
        self._tv.volumenDown()
    
    def volumenUp(self):
        self._tv.volumenUp()
    
    def setCanal(self, num):
        self._tv.setCanal(num)
    
    def enlazar(self, tv):
        self._tv = tv
        tv.control = self
    
    def setTv(self, tv):
        self._tv = tv
    
    def getTv(self):
        return self._tv