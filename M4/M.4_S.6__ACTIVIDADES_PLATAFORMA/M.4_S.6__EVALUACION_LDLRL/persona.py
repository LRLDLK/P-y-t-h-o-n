class Persona:
    def __init__(self, nombre, apellido, anno):
        self._nombre = nombre
        self._apellido = apellido
        self._anno = anno
    
    @property
    def _nombre(self):
        return self.nombre
    
    @_nombre.setter
    def _nombre(self, nombre):
        self.nombre = nombre
    
    @property
    def _anno(self):
        return self.anno
    
    @_anno.setter
    def _anno(self, anno):
        self.anno = anno
        
    @property
    def _apellido(self):
        return self.apellido
    
    @_apellido.setter
    def _apellido(self, apellido):
        self.apellido = apellido