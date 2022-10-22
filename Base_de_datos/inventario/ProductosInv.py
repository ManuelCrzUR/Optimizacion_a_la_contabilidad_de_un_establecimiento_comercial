class Productos:
    def __init__(self, Nombre:str, division:str, precio_unidad: int, cantiadad: int = 0) -> object:
        self.nombre = Nombre.upper()
        self.division = division.upper()
        self.precio_unitario = precio_unidad
        self.cantidad = cantiadad
        self.iva = False
        
    def __str__(self) -> str:
        mensaje = f"""PRODUCTO: {self.nombre}
PU: ${self.precio_unitario} - {self.cantidad} Unidades"""
        return mensaje
    
    def AñadirProducto(self, cantidad):
        self.cantidad += cantidad
        
    def RetirarProducto(self, cantidad):
        self.cantidad -= cantidad
        
    def ModificarPrecio(self, precio_nuevo):
        self.precio_unitario = precio_nuevo
        
    def SumarIva(self):
        impuesto = self.precio_unitario * 0.19
        self.precio_unitario += impuesto