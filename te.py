class Te:
    duracion = 365
    
    def __init__(self, sabor, formato):
        self.sabor = sabor
        self.formato = formato
        
    @staticmethod
    def obtener_tiempo_recomendacion(sabor):
        if sabor == 1: #"té negro":
            tiempo = 3
            recomendacion = "Consumir al desayuno"
        elif sabor == 2: #"té verde":
            tiempo = 5
            recomendacion = "Consumir al medio día"
        elif sabor == 3: #"infusión de hierbas":
            tiempo = 6
            recomendacion = "Consumir al atardecer"
        return tiempo, recomendacion
    
    @staticmethod
    def obtener_precio(formato):
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
        
    def obtener_sabor(self):
        if self.sabor == 1:
            texto = "té negro"
        elif self.sabor == 2:
            texto= "té verde"
            recomendacion = "Consumir al medio día"
        elif self.sabor == 3:
            texto = "infusión de hierbas"
            recomendacion = "Consumir al atardecer"
        return texto
    
    