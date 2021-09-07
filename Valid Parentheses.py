def valid_parentheses(string):
    filtered = "".join([i for i in string if i=="(" or i==")"])
    new_lst = []
    dicto = {
        ")":"("
    }
    for i in filtered:
        if i in dicto.values():
            new_lst.append(i)
        elif i in dicto.keys():
            if new_lst == [] or dicto[i]!= new_lst.pop():
                return False
        else:
            return False
    return new_lst == []
