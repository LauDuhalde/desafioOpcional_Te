from te import Te

sabor = int(input('''Selecciona el sabor de té: 
                     1. Té negro
                     2. Té verde
                     3. Agua de hierbas
                     >>>'''))
formato = int(input('Ingresa el formato 300g o 500g (sin g): '))

te = Te(sabor, formato)

print('El sabor del té es:',te.obtener_sabor()) #no requiere ingreso de parametros ya que usa la información de la instancia
print('El formato es de',formato,"gramos")
print(f'El precio es ${Te.obtener_precio(formato)}')
tiempo, recomendacion = Te.obtener_tiempo_recomendacion(sabor)
print('El tiempo de preparación es',tiempo,'minutos')
print('Se recomienda',recomendacion)
print('Tiene una duración de',Te.duracion,'días')
