"""
    O termo matemático Symetric Difference (t ou B) de 2 conjuntos é um conjunto de elementos
    no qualquer um dos conjuntos mas não em ambos. Por exemplo: A = {1,2,3} e B = {2,3,4},
    A E B = {1,4}

    Symetric difference é uma operação binária, isso significa que ela opera em apenas elementos.
    Então para avaliar uma expressão envolvendo symetric difference entre 3 elementos (A e B e C),
    você deve completar uma operação por vez. 
    Exemplo: C = {2, 3}, A e B e C = (A e B) e C = {1,4} e {2,3}


"""
def sym(*args):
    sym_diff = set()

    for item in args:
        if sym_diff:
           a = __sym_pair__(sym_diff, item)
           a.extend(__sym_pair__(item, sym_diff))
           sym_diff = a
        else:
            sym_diff = item

    return sorted(set(sym_diff))

def __sym_pair__(set_a, set_b):
    return [a for a in set_a if a not in set_b]