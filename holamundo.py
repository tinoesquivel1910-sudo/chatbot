from analizador import data

mensajeGenerico = """hola, soy tu chatbot de las entreadas del concierto                    
1:Horario del concierto
2:precio de las entradas
3:cuato estan?
4:si las quiero comprar
5:si las voy a comprar ahora
6: salir
"""

eleccion = int(input(mensajeGenerico))

while eleccion != 6:
    data(eleccion)
    eleccion = int(input(mensajeGenerico))