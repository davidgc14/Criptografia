# MiniAES pagina 19 tema 2

F.<x> = GF

def nibblesub(ll):
    xx = vector(ll)
    if xx != 0:
        xx = vector(reversed)