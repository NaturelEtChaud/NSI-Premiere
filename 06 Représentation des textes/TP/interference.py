def traitemnt(message_pollue):
    """
    Entrée :
        message_pollue est une chaîne de caractères
    Pré-condition :
        message_pollue n'est pas vide
    Sortie :
        message est une chaîne de caractères
    Post-condition :
        message ne comporte plus de . et tous les caractères entre deux * sont supprimés
    """
    message = ''
    i = 0
    asterix = False
    while i<len(message_pollue) :
        if message_pollue[i] == '*' :
            asterix = not asterix
        elif asterix == False and message_pollue[i] != '.' :
            message = message + message_pollue[i]
        i = i + 1
    return message
