class Departamento:
    def __init__(self, nombre_dpto, nombre_corto_dpto):
        self._nombre_dpto = nombre_dpto
        self._nombre_corto_dpto = nombre_corto_dpto

    @property
    def _nombre_dpto(self):
        return self.nombre_dpto
    
    @_nombre_dpto.setter
    def _nombre_dpto(self, nombre_dpto):
        self.nombre_dpto = nombre_dpto     

    @property
    def _nombre_corto_dpto(self):
        return self.nombre_corto_dpto
    
    @_nombre_corto_dpto.setter
    def _nombre_corto_dpto(self, nombre_corto_dpto):
        self.nombre_corto_dpto = nombre_corto_dpto    