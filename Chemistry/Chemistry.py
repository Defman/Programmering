import json


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
            if atom.name.upper() == search.upper() \
                    or atom.symbol == search:
                return atom
        raise LookupError("There is no symbol matching the search \"" + search + "\"")


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
        return self.symbol


class Molecule(object):
    def __init__(self, *atoms):
        self.atoms = [(s, atoms.count(s)) for s in set(atoms)]

    def __str__(self):
        return " ".join(map(lambda a: "_".join(map(str, a)), self.atoms))


def n(*molecules):
    return sum(map(lambda m: sum(map(lambda a: a[0].molar*a[1], m.atoms)), molecules))



table = PeriodicTable()
C = table.get_atom("C")
C2 = Molecule(*([C]*2))

print(n(C2))