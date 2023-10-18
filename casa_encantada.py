import random
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

mansion = [
    ["⬜️","⬜️","⬜️","⬜️"],
    ["⬜️","⬜️","⬜️","⬜️"],
    ["⬜️","⬜️","⬜️","⬜️"],
    ["⬜️","⬜️","⬜️","⬜️"],
]
def set_door_pos(mansion):
    door = "🚪";
    door_pos_x = random.randint(0, 3)
    door_pos_y = random.randint(0, 3)
    
    mansion[door_pos_y][door_pos_x] = door
    
    return mansion

def set_ghost_pos(mansion):
    ghost = "👻"
    while True:
        ghost_pos_x = random.randint(0,3)
        ghost_pos_y = random.randint(0,3)
        position = mansion[ghost_pos_y][ghost_pos_x]
        
        if position != "🚪":
            mansion[ghost_pos_y][ghost_pos_x] = ghost
            break
        
    return mansion  

def set_candy_pos(mansion):
    candy = "🍭"
    while True:
        candy_pos_x = random.randint(0,3)
        candy_pos_y = random.randint(0,3)
        position = mansion[candy_pos_y][candy_pos_x]
        
        if position != "🚪" and position != "👻":
            mansion[candy_pos_y][candy_pos_x] = candy
            break
        
    return mansion 

def set_player_pos(mansion):
    player = "👤"
    while True:
        player_pos_x = random.randint(0,3)
        player_pos_y = random.randint(0,3)
        position = mansion[player_pos_y][player_pos_x] 
        
        if position != "🚪" and position != "👻" and position != "🍭":
            mansion[player_pos_y][player_pos_x] = player
            break
        
    return mansion 

#Inicializamos la mansion seteando las posiciones del fantasma, la puerta y la habitacion de dulces
mansion = set_door_pos(mansion)
mansion = set_ghost_pos(mansion)
mansion = set_candy_pos(mansion)
mansion = set_player_pos(mansion)

for i in mansion:
    print(i)

#print(mansion)

