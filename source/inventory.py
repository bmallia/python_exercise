
"""
        Compare e atualize o inventário carrega num array 2D de uma entrega nova.
        Atualize a quantidade de itens existentes no array atual (no arr1)
        se um item não for encontrado, adicione um item novoe e a quantidade dentro do 
        array de inventario
        o array retornado de inventário deve estar em ordem alfabética

        1. encontra elemento de arr2 em arr1
        2. se existir, atualiza item do inventário
        3. senão adiciona elemento no arr1     
"""
def updateInventory(arr1, arr2):
    elements_name = [elem[1] for elem in arr1]

    for _, elem2 in enumerate(arr2):
        if elem2[1] in elements_name:
            index = elements_name.index(elem2[1])
            arr1[index][0] += elem2[0]
        else:
            arr1.append(elem2)
            elements_name = [elem[1] for elem in arr1]
            
    
    return Sort(arr1)

##código python para ordenar as tuplas usando o segundo elemento da sublista
    """
        Ordena as tuplas usando o segundo elemento da lista        
    """
def Sort(sub_list):
    sub_list.sort(key = lambda x: x[1])
    return sub_list
