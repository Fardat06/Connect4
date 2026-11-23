class Tabla:
    def __init__(self):
        self.celula = [[".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."]]

    def afisare(self):
        print(" 1 | 2 | 3 | 4 | 5 | 6 | 7 |")

        for rand in self.celula:
            print(" " + " | ".join(rand) + " |")

    def urmatorulpas(self, jucator, numarcoloana):
        if numarcoloana < 1 or numarcoloana > 7:
            print("Alege o coloana intre 1 si 7!")
            return False

        coloana = numarcoloana - 1

        for rand in range(5, -1, -1):
            if self.celula[rand][coloana] == ".":
                self.celula[rand][coloana] = jucator
                return True

        #print("Coloana este plina!")
        return False

    def castigator(self, jucator):
        for rand in range(6):
            for coloana in range(4):
                if (self.celula[rand][coloana] == jucator and
                    self.celula[rand][coloana + 1] == jucator and
                    self.celula[rand][coloana + 2] == jucator and
                    self.celula[rand][coloana + 3] == jucator):
                    return True

        for rand in range(3):
            for coloana in range(7):
                if (self.celula[rand][coloana] == jucator and
                    self.celula[rand + 1][coloana] == jucator and
                    self.celula[rand + 2][coloana] == jucator and
                    self.celula[rand + 3][coloana] == jucator):
                    return True

        for rand in range(3):
            for coloana in range(4):
                if (self.celula[rand][coloana] == jucator and
                    self.celula[rand + 1][coloana + 1] == jucator and
                    self.celula[rand + 2][coloana + 2] == jucator and
                    self.celula[rand + 3][coloana + 3] == jucator):
                    return True

        for rand in range(3, 6):
            for coloana in range(4):
                if (self.celula[rand][coloana] == jucator and
                    self.celula[rand - 1][coloana + 1] == jucator and
                    self.celula[rand - 2][coloana + 2] == jucator and
                    self.celula[rand - 3][coloana + 3] == jucator):
                    return True

        return False

    def egalitate(self):
        for coloana in range(7):
            if self.celula[0][coloana] == ".":
                return False

        return True

    def mesajdeinceput(self):
        print("Bun venit la jocul Connect 4")


def minimax(tabla, adancime, este_maximizare):

    if tabla.castigator("X"):
        return 10-adancime

    if tabla.castigator("0"):
        return adancime-10

    if tabla.egalitate():
        return 0

    if adancime == 5:
        return 0

    if este_maximizare:
        cel_mai_bun_scor = -1000

        for coloana in range(1, 8):

            if tabla.urmatorulpas("X", coloana):

                scor = minimax(tabla, adancime + 1, False)

                for rand in range(6):
                    if tabla.celula[rand][coloana - 1] == "X":
                        tabla.celula[rand][coloana - 1] = "."
                        break

                cel_mai_bun_scor = max(cel_mai_bun_scor, scor)

        return cel_mai_bun_scor

    else:
        cel_mai_bun_scor = 1000

        for coloana in range(1, 8):

            if tabla.urmatorulpas("0", coloana):

                scor = minimax(tabla, adancime + 1, True)

                for rand in range(6):
                    if tabla.celula[rand][coloana - 1] == "0":
                        tabla.celula[rand][coloana - 1] = "."
                        break

                cel_mai_bun_scor = min(cel_mai_bun_scor, scor)

        return cel_mai_bun_scor


def mutare_computer(tabla):

    cel_mai_bun_scor = 1000
    cea_mai_buna_mutare = None

    for coloana in range(1, 8):

        if tabla.urmatorulpas("0", coloana):

            scor = minimax(tabla, 0, True)

            for rand in range(6):
                if tabla.celula[rand][coloana - 1] == "0":
                    tabla.celula[rand][coloana - 1] = "."
                    break

            if scor < cel_mai_bun_scor:
                cel_mai_bun_scor = scor
                cea_mai_buna_mutare = coloana

    tabla.urmatorulpas("0", cea_mai_buna_mutare)

    print("\nComputerul a ales coloana:", cea_mai_buna_mutare)


tabla = Tabla()

tabla.mesajdeinceput()

print("\nTu esti X.")
print("Computerul este 0.")

tabla.afisare()


while True:

    while True:
        try:
            alegeraluix = int(input("\nX) Alege o coloana de la 1 la 7: "))

            if tabla.urmatorulpas("X", alegeraluix):
                break

        except ValueError:
            print("Te rog introdu un numar!")

    tabla.afisare()

    if tabla.castigator("X"):
        print("X este castigatorul!")
        break

    if tabla.egalitate():
        print("Este egalitate!")
        break

    print("\nComputerul gandeste...")

    mutare_computer(tabla)

    tabla.afisare()

    if tabla.castigator("0"):
        print("0 este castigatorul!")
        print("Computerul a castigat!")
        break

    if tabla.egalitate():
        print("Este egalitate!")
        break
