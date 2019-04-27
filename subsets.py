def get_subsets(array):
    if len(array)==0:
        return [[]]
    else:
        res = get_subsets(array[:-1])
    extra = array[-1]
    new = []
    for el in res:
        new.append(el+[extra])
    return new+res
print(get_subsets([1,2,3]))