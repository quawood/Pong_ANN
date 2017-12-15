def List_Amount(List):
    return _List_Amount(List)

def _List_Amount(List):
    counter = 0
    if isinstance(List, list):
        for l in List:
            c = List_Amount(l)
            counter += c
        return counter
    else:
        return 1