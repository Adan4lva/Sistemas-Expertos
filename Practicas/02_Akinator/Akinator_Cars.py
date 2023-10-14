class Nodo:
    def __init__(self, pregunta=None, si=None, no=None, personaje=None):
        self.pregunta = pregunta
        self.si = si
        self.no = no
        self.personaje = personaje


def adivina_personaje(arbol):
    nodo_actual = arbol


    while nodo_actual.pregunta:
        respuesta = input(nodo_actual.pregunta + " (si/no): ").lower()
        if respuesta == "si":
            nodo_actual = nodo_actual.si
        else:
            nodo_actual = nodo_actual.no

    if nodo_actual.personaje:
        print("¡Adiviné! El personaje es", nodo_actual.personaje)


    else:
        print("No pude adivinar el personaje. ¿Quién era?")
        nuevo_personaje = input("Nombre del personaje: ")
        nueva_pregunta = input(f"Por favor, dame una pregunta que distinga a {nuevo_personaje} de {nodo_actual.personaje}: ")
        respuesta_nueva_pregunta = input(f"¿Cuál es la respuesta para {nuevo_personaje}? (sí/no): ").lower()
        if respuesta_nueva_pregunta == "sí":
            nodo_actual.pregunta = nueva_pregunta
            nodo_actual.si = Nodo(personaje=nuevo_personaje)
            nodo_actual.no = Nodo(personaje=nodo_actual.personaje)
        else:
            nodo_actual.pregunta = nueva_pregunta
            nodo_actual.si = Nodo(personaje=nodo_actual.personaje)
            nodo_actual.no = Nodo(personaje=nuevo_personaje)


# Crear un árbol de decisión inicial
arbol = Nodo("¿Es un personaje de Cars?")
arbol.si = Nodo("¿Es un coche rojo?")
arbol.no = Nodo("¿Es un coche azul?")
arbol.si.si = Nodo(personaje="Rayo McQueen")
arbol.no.si = Nodo(personaje="Sally")
arbol.no.no = Nodo(personaje="Mate")


# Jugar el juego
print("Piensa en un personaje de Cars y yo trataré de adivinarlo.")
while True:
    adivina_personaje(arbol)
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ").lower()
    if jugar_de_nuevo != "si":
        break