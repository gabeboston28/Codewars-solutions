import string
def pig_it(text):
    newlst=[]
    for i in text.split():
        newchar = i+i[0]
        new=""
        for j in range(len(newchar)):
            if j!=0:
                new+=newchar[j]
                if newchar[j] not in string.punctuation:
                    freshchar = new+"ay"
                else:
                    freshchar = new
        newlst.append(freshchar)
    return " ".join(newlst)
