import string
import math
import numpy as np
from . import atomic_units as au
from .elements import Element, PeriodicTable

class Atom:
    _cfact={'au2m' : au.au2m, 'au2nm' : au.au2nm,
            'au2a' : au.au2a, 'au2pm' : au.au2pm,
            'None' : 1, 'none' : 1, 'a2au' : au.a2au, 'nm2au' : au.nm2au,
            'pm2au' : au.pm2au}
    coord=(0,0,0)
    conv=_cfact['None']

    def __init__(self, coord=(0,0,0), sym='None'):
        self.coord=np.array(coord)
        self._setelement(sym)

    def __add__(self, other):
        return Atom(self.coord + other.coord)

    def __sub__(self, other):
        return Atom(self.coord - other.coord)

    def __str__(self):
        s = self.element.symbol
        for i in range(3):
            s += ' ' + str(self.coord[i])
        return s

    def __repr__(self):
        s='{Atom: ' + self.element.name + ' at ' + str(self.coord) + '}'
        return s

    def bond_distance(self, atom):
        dist = atom - self
        return np.linalg.norm(dist.coord)

    def get_coord(self):
        return self.coord

    def _setelement(self, s):
        s=string.lower(s)
        try:
            self.element=PeriodicTable[s]
        except KeyError as x:
            print("Invalid element:", x);

    def change_units(self, conv):
        self.coord *= self._cfact[conv]

if __name__ == '__main__':
    a1 = Atom((10,10,10))
    a2 = Atom((9,9,9))
    print(a1 - a2)
    print(a1.bond_distance(a2))

# vim:et:ts=4:sw=4
