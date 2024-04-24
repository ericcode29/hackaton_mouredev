from enum import Enum

class Color(Enum):
    verde_claro = '#e6ffcb'
    verde = '#b3df9c'
    verde_base = '#7fbf6d'
    verde_medio = '#4c9f3e'
    verde_oscuro = '#187f0f'

    negro = '#000000'
    negro_claro = '#242424'
    gris_oscuro = '#474747'
    gris = '#6b6b6b'
    gris_claro = '#8e8e8e'


class Size(Enum):
    default = '12em'
    mediano = '16em'
    grande = '20em'
    sm = '30em',
    md = '48em',
    lg = '62em',
    xl = '80em',
    xxl = '96em',