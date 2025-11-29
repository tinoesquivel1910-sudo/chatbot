def data(eleccion):
    if eleccion == "1":
        total = "las clases empiezan a las 10:00 y terminan a las 11:30"
    elif eleccion == "2":
       print("las clases cuestan 45.000 pesos al mes")
    elif eleccion == "3":
        print("el profe no tiene telefono(al menos no publico)")
    else:
        print("no te entiendo")

eleccion = int(input("""hola, soy un chatbot. estas son las preguntas que puedes hacerme:
                    1: horarios de clase
                     2:precio de clases
                     3:telefono del profe
                     4: salir""" ))
while eleccion != 4:
    data(eleccion)
    print("""hola, soy un chatbot. estas son las preguntas que puedes hacerme:
                    1: horarios de clase
                     2:precio de clases
                     3:telefono del profe
                     4: salir""")