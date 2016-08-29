import json

class Unit(float):
    pass


class Atom(object):
    def __init__(self, name, electrons, position, molar, group, number, symbol):
        self.name = name
        self.electrons = electrons
        self.position = position
        self.molar = molar
        self.group = group
        self.number = number
        self.symbol = symbol

    def __str__(self):
        return json.dumps(self.__dict__)


class PeriodicTable(object):
    def __init__(self):
        self.atoms = []
        with open("periodicTable.json") as data:
            for period in json.load(data)["table"]:
                for element in period["elements"]:
                    self.atoms.append(Atom(
                        element["name"],
                        element["electrons"],
                        element["position"],
                        element["molar"],
                        element["group"],
                        element["number"],
                        element["small"]))

    def get_atom(self, search):
        for atom in self.atoms:
            if atom.symbol == search.upper() or atom.symbol == search:
                return atom
        raise LookupError("There is no symbol matching the search \"" + search + "\"")


class Molecule(object):
    def __init__(self, atoms):
        self.atoms = atoms

    def __str__(self):
        symbols = sorted(map(lambda atom: atom.symbol, self.atoms))
        result = ""
        for s in symbols:
            count = symbols.count(s)
            result += s + count
            symbols.remove(s)
        return result


class mol(Unit):
    def __init__(self, substance):
        self.substance = substance

    def __str__(self):
        return str(self.substance) + " mol"


def x(atom, molecules):
    return n(atom)/sum(map(lambda m: n(m), molecules))


def p(V, n, T, R=8.314472):
    return n*R*T/V


def n(x, mass=1):
    if type(x) is Molecule:
        return mol(mass/sum(map(lambda a: a.molar, x.atoms)))
    return mol(mass/x.molar)

table = PeriodicTable()

N = table.get_atom("N")
N2 = Molecule([N, N])
H = table.get_atom("H")
H2 = Molecule([H, H])
C = table.get_atom("C")
O = table.get_atom("O")
CO2 = Molecule([C, O, O])

print(p(10, n(H2, 1.43)+n(N2, 5.72)+n(CO2, 20.2), 293.15))

print(x(H2, [H2, N2, CO2]))

print(CO2)