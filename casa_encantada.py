import random, keyboard
"""
 * Este es un reto especial por Halloween.
 * Te encuentras explorando una mansión abandonada llena de habitaciones.
 * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 * Tu misión es encontrar la habitación de los dulces.
 *
 * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 * (Tienes total libertad para ser creativo con los textos)
 *
 * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 *   Esta podría ser una representación:
 *   🚪⬜️⬜️⬜️
 *   ⬜️👻⬜️⬜️
 *   ⬜️⬜️⬜️👻
 *   ⬜️⬜️🍭⬜️
 * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 *   Si no lo aciertas no podrás desplazarte.
 * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 *   tengas que responder dos preguntas para salir de ella.
 */
"""
enigmas = {
    "Si me nombras, dejo de existir. ¿Quién soy?":  "El silencio",

    "Puedes sostenerme en tu mano, pero no me puedes retener mucho tiempo. ¿Qué soy?":  "El agua",

    "Soy más poderoso que Dios, más malévolo que el diablo, los ricos lo necesitan y los pobres lo tienen. Si lo comes, morirás. ¿Qué soy?":  "Nada",

    "Cuanto más lo quites, más grande se vuelve. ¿Qué es?":  "Un agujero",

    "Siempre estoy delante de ti, pero no puedes verme. ¿Qué soy?":  "El futuro",

    "Tengo ciudades, pero no tengo casas. Tengo bosques, pero no tengo árboles. Tengo ríos, pero no tengo agua. ¿Qué soy?": "Un mapa",

    "Siempre subo, pero nunca bajo. Nunca me puedes tocar, pero aún puedes sentirme. ¿Qué soy?":  "Tu edad",

    "Siempre va hacia adelante, pero nunca llega a su destino. ¿Qué es?":  "El tiempo",

    "Adivina quién soy: Tengo ramas, pero no hojas, tengo un tronco, pero no soy un árbol. ¿Quién soy?": "Un rio",

    "A veces soy líquido, a veces soy sólido, a veces soy gas. ¿Qué soy?": "El agua",

    "Cuanto mas lo lavas mas sucio se vuelve. ¿Que soy?": "El jabon",

    "No soy vivo pero crezco, no tengo pulmones pero necesito aire, no tengo boca pero el agua me mata. ¿Que soy?": "El fuego",

    "*Cuanto más lo tomas, más sed tienes. ¿Qué es?": "Agua salada",

    "Puedes romperme sin tocarme ni verme. ¿Qué soy?": "Un silencio",

    "Tienes que romperme antes de que pueda utilizarme. ¿Qué soy?": "Un huevo",

    "Mi vida puede ser medida en horas, soy débil, pero también fuerte, me derretiré con facilidad y puedo romper cristal. ¿Qué soy?": "Un hielo",

    "Tengo dientes pero nunca muerdo. ¿Qué soy?": "Un peine",

    "Soy un número que cuando lo volteas, sigue siendo el mismo. ¿Qué número soy?": "8 Ocho",

    "Cuantos ladrillos se necesitan para completar un edificio": "1 Uno",

    "Las mujeres no la tienen, pero los hombres sí. Los toros tienen dos, igual que un obispo. ¿Qué soy?": "La letra O",

    "Hay algo que, aunque te pertenezca, la gente siempre lo utiliza más que tú. ¿Qué es?": "Tu nombre",

    "Las personas siempre duermen menos en un mes del año. ¿Cuál es este mes?": "Febrero",

    "¿Cuántos 9 hay entre el 1 y el 100?": "Veinte 20"
}
door = "🚪";
ghost = "👻"
candy = "🍭"
player = "👤"
mansion = [
    ["⬜️","⬜️","⬜️","⬜️"],
    ["⬜️","⬜️","⬜️","⬜️"],
    ["⬜️","⬜️","⬜️","⬜️"],
    ["⬜️","⬜️","⬜️","⬜️"],
]


MOVE_NORTH = lambda pos_player_y: player_pos_y - 1
MOVE_SOUTH = lambda pos_player_y: player_pos_y + 1
MOVE_EAST = lambda pos_player_x: pos_player_x + 1
MOVE_WEST = lambda pos_player_x: pos_player_x - 1


def set_door_pos(mansion):
    door = "🚪";
    door_pos_x = random.randint(0, 3)
    door_pos_y = random.randint(0, 3)

    mansion[door_pos_y][door_pos_x] = door

    return mansion, door_pos_y, door_pos_x

def set_new_player_pos(player_pos_y, player_pos_x):
    mansion[player_pos_y][player_pos_x] = player

def set_ghost_pos(mansion):
    ghost = "👻"
    while True:
        ghost_pos_x = random.randint(0,3)
        ghost_pos_y = random.randint(0,3)
        position = mansion[ghost_pos_y][ghost_pos_x]

        if position != "🚪":
            mansion[ghost_pos_y][ghost_pos_x] = ghost
            break

    return mansion, ghost_pos_y, ghost_pos_x

def set_candy_pos(mansion):
    candy = "🍭"
    while True:
        candy_pos_x = random.randint(0,3)
        candy_pos_y = random.randint(0,3)
        position = mansion[candy_pos_y][candy_pos_x]

        if position != "🚪" and position != "👻":
            mansion[candy_pos_y][candy_pos_x] = candy
            break

    return mansion, candy_pos_y, candy_pos_x

def set_player_pos(mansion):
    player = "👤"
    while True:
        player_pos_x = random.randint(0,3)
        player_pos_y = random.randint(0,3)
        position = mansion[player_pos_y][player_pos_x]

        if position != "🚪" and position != "👻" and position != "🍭":
            mansion[player_pos_y][player_pos_x] = player
            break

    return mansion, player_pos_y, player_pos_x

def has_ghost(pos_y, pos_x):
    if mansion[pos_y][pos_x] == mansion[ghost_pos_y][ghost_pos_x]:
        return True
    else:
        return False

def has_candy(pos_y, pos_x):
    if mansion[pos_y][pos_x] == mansion[candy_pos_y][candy_pos_x]:
        return True
    else:
        return False


def show_possible_moves(player_pos_y, player_pos_x):

    max_y, max_x = 3, 3

    movimientos = []

    if player_pos_y > 0:
        if not mansion[player_pos_y - 1][player_pos_x] == "❌":
            movimientos.append("flecha arriba")


    if player_pos_y < max_y:
        if not mansion[player_pos_y + 1][player_pos_x] == "❌":
            movimientos.append("flecha abajo")


    if player_pos_x < max_x:
        if not mansion[player_pos_y][player_pos_x + 1] == "❌":
            movimientos.append("flecha derecha")


    if player_pos_x > 0:
        if not mansion[player_pos_y][player_pos_x - 1] == "❌":
            movimientos.append("flecha izquierda")

    return movimientos






#Inicializamos la mansion seteando las posiciones del fantasma, la puerta y la habitacion de dulces
mansion = set_door_pos(mansion)
mansion, door_pos_y, door_pos_x = mansion
print(f"[{door_pos_y}][{door_pos_x}]")

mansion = set_ghost_pos(mansion)
mansion, ghost_pos_y, ghost_pos_x = mansion
print(f"[{ghost_pos_y}][{ghost_pos_x}]")

mansion = set_candy_pos(mansion)
mansion, candy_pos_y, candy_pos_x = mansion
print(f"[{candy_pos_y}][{candy_pos_x}]")

mansion = set_player_pos(mansion)
mansion, player_pos_y, player_pos_x = mansion
print(f"[{player_pos_y}][{player_pos_x}]")


for i in mansion:
    print("".join(i))


# Cambiamos los objetos por cuadros blancos para camuflarlos y que el usuario no los vea
mansion[ghost_pos_y][ghost_pos_x] = "⬜"
mansion[candy_pos_y][candy_pos_x] = "⬜"
mansion[door_pos_y][door_pos_x] = "⬜"


#Mostramos al usuario el primer enigma para que pueda cambiar de habitación
print("/*/*/*/*/*/*/ La respuesta a la pregunta debe de ser con UNA sola PALABRA \*\*\*\*\*\*")
acertijo = random.choice(list(enigmas.keys()))
respuesta = input( f"{acertijo} -> ")


while True:
    if respuesta.lower() in enigmas.get(acertijo).lower():
        print("¡¡Has acertado!!") #Ejecutar logica de si acierta la pregunta
        possible_moves = show_possible_moves(player_pos_y, player_pos_x)

        print(f"Tus posibles movimientos son: {possible_moves}")

        # Controlamos que el usuario se mueva solo a donde es posible
        while True:
            key = keyboard.read_event()
            if key.event_type == keyboard.KEY_DOWN:
                if key.name in show_possible_moves(player_pos_y, player_pos_x):
                    break
                else:
                    print("No puedes ir en esa dirección.")

        # Cerramos la habitacion donde estaba el jugador
        mansion[player_pos_y][player_pos_x] = '❌'

        if key.name == "flecha arriba":
            player_pos_y = MOVE_NORTH(player_pos_y)
        elif key.name == "flecha abajo":
            player_pos_y = MOVE_SOUTH(player_pos_y)
        elif key.name == "flecha derecha":
            player_pos_x = MOVE_EAST(player_pos_x)
        elif key.name == "flecha izquierda":
            player_pos_x = MOVE_WEST(player_pos_x)

        # Colocamos al jugador en la nueva posicion
        set_new_player_pos(player_pos_y, player_pos_x)

        #Verificamos si en la nueva posicion
        if has_ghost(player_pos_y, player_pos_x):
            # Tenemos que hacer 2 preguntas
            while True:
                correct_answers = 0
                acertijo1 = random.choice(list(enigmas.keys()))
                respuesta = input(f"{acertijo} -> ")
                if respuesta.lower() in enigmas.get(acertijo).lower():
                    acertijo = random.choice(list(enigmas.keys()))
                    respuesta = input(f"{acertijo} -> ")
                    correct_answers += 1
                else:
                    print("Respuesta Incorrecta")
                    correct_answers = 0
                if correct_answers == 2:
                    print("Respuestas Correctas")
                    break



        for room in mansion:
            print(room)
else:
    print("¡¡Has fallado!!")





