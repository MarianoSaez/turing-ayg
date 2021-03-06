"""
Esta clase simula las acciones de una maquina de Turing con una
serie de restricciones en sus parametros.
Restricciones:
    - Las entradas no pueden contener el simbolo blanco (por definicion)
    - Esta maquina de Turing es deterministica por lo que no pueden
      existir dos transiciones para un mismo par estado-simbolo
    - No deben existir transiciones desde los estados finales (POSIBLEMENTE SOLUCIONADO)
"""
from table import Table


class TM:
    # Constructor de Maquina de Turing
    # Definicion formal de una TM:
    #   M = ( Q, S, G, start, F, blank, delta )
    #   Donde:
    #       Q es el conjunto de estados de la TM
    #       S es el alfabeto de input
    #       G es el alfabeto de la cinta (incluye al blank)
    # ========== Aca comienzan args del constructor usados ===========
    #       start es el estado inicial
    #       F es el conjunto de estados finales
    #       blank es el simbolo blanco (pertence a G y no a S)
    #       delta es la funcion de transicion
    def __init__(self, start, F, blank, delta, cinta=""):
        self.start = start
        self.F = F
        self.blank = blank
        self.delta = delta
        self.tabla = Table("ESTADO ACTUAL:SIMBOLO ACTUAL:SIG. ESTADO:SIMBOLO ESCRITO:MOVIMIENTO".split(":"))
        self.cinta = cinta

    @property
    def cinta(self):
        return self._cinta

    @cinta.setter
    def cinta(self, value):
        self._cinta = list()
        for i in value:
            self._cinta.append(i)
        self._cinta.append(self.blank)
        self.tabla.rows = list()

    def get_terna(self, state, simbol):
        try:
            return self.delta[state + simbol].split()
        except KeyError:
            return "Undefined Undefined Undefined".split()

    def seek_next_terna(self, state, simbol):
        if state + simbol in self.delta:
            return True
        return False


    # Funcion principal encargada de computar cadenas de entrada a
    # la maquina de Turing. Agrega cada configuracion a la tabla
    # de la MT.
    # Retorna True o False segun si la cadena es o no es computable.
    def compute(self):
        curr_state = self.start
        i = 0
        while i < len(self.cinta):
            # Leer simbolo de la cinta
            curr_simbol = self.cinta[i]

            # Construimos la fila para la tabla [display]
            row = [curr_state, curr_simbol]

            # Determinar si es un estado de aceptacion o rechazo
            if not self.seek_next_terna(curr_state, curr_simbol):
                if curr_state in self.F:
                    return True
                else:
                    return False

            # Obtener imagen para el par (curr_state, curr_simbol)
            curr_state, w_simbol, move = self.get_terna(curr_state, curr_simbol)

            # Agregamos ultimos campos a la fila de la tabla [display]
            row.append(curr_state)
            row.append(w_simbol)
            row.append(move)

            # Escribir simbolo en la cinta
            self.cinta[i] = w_simbol

            # Mover cabezal
            if move == "R":
                i += 1
            elif move == "L":
                i -= 1
            else:
                # Caso de TM extendida d: Q x G --> Q x G x { R, L, S }
                i = i

            # Agregamos la fila a la tabla asociada
            self.tabla.rows.append(row)

    # Funcion encargada de imprimir la linea final que indica si
    # la cadena es valida o no
    def resume(self, computable):
        valid = " ES UNA CADENA VALIDA "
        not_valid = " NO ES UNA CADENA VALIDA "
        print(self.tabla)
        if computable:
            print(valid.center(88, "="))
        else:
            print(not_valid.center(88, "="))


# Codigo de prueba
if __name__ == "__main__":
    # start = "A"
    # F = ["F"]
    # blank = "#"
    # delta = {
    #     "Aa": "B a R",
    #     "Ab": "C b R",
    #     "Ba": "D a R",
    #     "Bb": "C b R",
    #     "B#": "F # L",
    #     "C#": "F # L",
    #     "Da": "D a R",
    #     "Db": "C b R"
    # }
    start = "q0"
    F = ["q1"]
    blank = "#"
    delta = {
        "q00": "q1 # R",
        "q01": "q0 # R",
        "q10": "q0 # R",
        "q11": "q1 # R"
    }
    entrada = "1100"

    M = TM(start, F, blank, delta)
    M.cinta = entrada

    result = M.compute()
    M.resume(result)
