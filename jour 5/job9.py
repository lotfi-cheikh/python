L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
def val(L):
    Vmin = L[0]
    Vmax = L[0]
    for i in L:
        if i > Vmax:
            Vmax = i
        if i < Vmin:
            Vmin = i
    return Vmax,Vmin
print(val(L))