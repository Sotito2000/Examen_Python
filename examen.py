from libro import Libro
from autor import Autor

class Examen:
    def get_list(fichero):
        dic = dict()
        if len(fichero) == 0:
                raise ValueError("El fichero esta vacio.")
        else:
            dic = {'1': fichero[0], '2': fichero[1], '3': fichero[2]}
        return dic

    def mas_antiguos(lista, anyo):
        if anyo < 1900 or anyo > 2021:
            raise ValueError("El anyo no es valido")