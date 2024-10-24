meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "GG": "Good Game, que significa buen juego en inglés"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print("no tenemos la palabra disponible")
    # ¿Qué hacer si no se encuentra la palabra?
