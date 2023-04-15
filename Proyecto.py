import random
Luchadores = ["1. Spiderman", "2. Iron man", "3. Capitan America", "4. Batman", "5. Mujer Maravilla", "6. Hulk", "7. Thor" ]
liga_DC = {"Spiderman": {"Fuerza": 100, "Resistencia" : 90},
           "Iron man" : {"Fuerza": 90, "Resistencia" : 70},
           "Capitan america": {"Fuerza": 70, "Resistencia" : 80},
           "Batman" : {"Fuerza": 70, "Resistencia" : 50},
           "Mujer maravilla" : {"Fuerza": 85, "Resistencia" : 83},
           "Hulk" : {"Fuerza": 95, "Resistencia" : 90},
           "Thor" : {"Fuerza": 92, "Resistencia" : 88},}
#Funcion para el Vs con la computadora
def computadora():
    print("Lista de Super Héroes ")
    for i in Luchadores:
        print(i)
        #Selección de personaje
    luchador_1  = input("Elije tu luchador: ").capitalize()
    if luchador_1 in liga_DC.keys():
        #Hacer de manera random la selección de la computadora
        computadora, caracteristis_v2 = random.choice(list(liga_DC.items()))
        print(f"Luchador de la Computadora: {computadora}")
        print(f"{luchador_1} Vs {computadora}")
        #Evaluar el ganador de la batalla
        if luchador_1 > computadora:
            print(f"{computadora} ocasionó algunos daños pero no fueron suficientes para el poder de {luchador_1} ")
            print(f"El ganador de la batalla es: {luchador_1}")
        elif computadora > luchador_1:
            print(f"{luchador_1} ocasionó algunos daños pero no fueron suficientes para el poder de {computadora} ")
            print(f"El ganador de la batalla es: {computadora}")
        else:
            print("Ambos tienen las mismas caracteristicas, ¡la batalla quedó en empate!")
#Funcion para Jugador 1 vs Jugador 2
def dos_jugadores():
    print("Lista de Super Héroes ")
    for i in Luchadores:
        print(i)
    #Selección de personajes
    luchador_1  = input("Jugador 1, Elije tu luchador: ").capitalize()
    luchador_2  = input("Jugador 2, Elije tu luchador: ").capitalize()
    if luchador_1 and luchador_2 in liga_DC.keys():
        print(f"{luchador_1} Vs {luchador_2}")
        #Evaluar el ganador de la batalla
        if luchador_1 > luchador_2:
            print(f"{luchador_2} no pudo con los ataques violentos de {luchador_1}")
            print(f"El ganador de la batalla es: {luchador_1}")
        elif luchador_2 > luchador_1:
            print(f"{luchador_1} no pudo con los ataques violentos de {luchador_2}")
            print(f"El ganador de la batalla es: {luchador_2}")
        else:
            print("Ambos tienen las mismas caracteristicas, ¡la batalla quedó en empate!")
    else:
        print("El luchador no está en la lista")
#Menú de inicio         
print("Bienvenidos a la LIGA DC")
print("1. Vs Computadora")
print("2. Dos jugadores")
pregunta = int(input("Que modo deseas jugar?: "))
if pregunta == 1:
    computadora()
elif pregunta == 2:
    dos_jugadores()
else:
    print("Esta opción no está en el menú")