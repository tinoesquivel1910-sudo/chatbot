def data(eleccion):
    if eleccion == "1":
        total="el concirto empiza a las 22:30"
    elif eleccion =="2":
        print("las entradas cuestan 60.000")
    elif eleccion =="3":
        print("no hay enntradas suficientes,va a tener q ir reventa")
    else:
        print("cuanto cuestan las entradas de reventa?")
eleccion = int(input(""" hola, soy tu chatbot de las entreadas del concierto                    
                            1:Horario del concierto
                            2:precio de las entradas
                            3:cuato estan?
                            4:salir"""))
