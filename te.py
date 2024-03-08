class Te:
    duracion = 365
    
    def __init__(self, sabor, formato): #Constructor
        self.sabor = sabor
        self.formato = formato
        
    @staticmethod
    def obtener_tiempo_recomendacion(sabor):
        """
        Define y retorna el tiempo de preparación y recomendadción de consumo del té según su sabor
        ------------
        Parameter
        ------------
        sabor
            Type:   int
            Posibles valores:    1, 2, 3
        
        Return
        ------------
        tiempo
            Type:   int
            Descripción:    Tiempo de preparación del té
        recomendacion
            Type:   string
            Descripción:    Momento del día en que se recomienda su consumo
        """
        if sabor == 1: #"té negro"
            tiempo = 3
            recomendacion = "Consumir al desayuno"
        elif sabor == 2: #"té verde"
            tiempo = 5
            recomendacion = "Consumir al medio día"
        elif sabor == 3: #"infusión de hierbas"
            tiempo = 6
            recomendacion = "Consumir al atardecer"
        return tiempo, recomendacion
    
    @staticmethod
    def obtener_precio(formato):
        """
        Define y retorna el valor del té según su formato
        ------------
        Parameter
        ------------
        formato
            Type:   int
            Posibles valores:    300 o 500
            Descripción: Formato de té a comprar que puede ser 300g o 500g
        
        Return
        ------------
        precio
            Type:   int
            Descripción:    Precio a pagar por el té
        """
        if formato == 300:
            precio = 3000
        elif formato == 500:
            precio = 5000
        return precio
        
    def obtener_sabor(self): #self es similar a this en java, se usa para referenciar la instancia actual
        """
        Define y retorna el nombre del sabor de té
        ------------
        Parameter
        ------------
        formato
            Type:   int
            Posibles valores:    1, 2, 3
        
        Return
        ------------
        texto
            Type:   string
            Posibles valores:    té negro, té verde o infusión de hierbas
        """
        if self.sabor == 1:
            texto = "té negro"
        elif self.sabor == 2:
            texto= "té verde"
            recomendacion = "Consumir al medio día"
        elif self.sabor == 3:
            texto = "infusión de hierbas"
            recomendacion = "Consumir al atardecer"
        return texto
    
    
    