L = [8, 24,48,2,16]
def multiple(L):
    A = 0
    for i in L:
        if i%3 == 0:
            A = A + 1
    return A
print(multiple(L))
            
