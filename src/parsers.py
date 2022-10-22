from datetime import datetime
#lo ponemos en otro archivo porque es mas facil su reutilización
def parse_fecha(cadena,formato="%d/%m/%Y"):
    return datetime.strptime(cadena,formato)