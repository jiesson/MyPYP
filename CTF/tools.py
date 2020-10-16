import random
def getstr(n):
    re=""
    for i in range(n):
        s=random.randint(48,122)
        #32-126---all
        #48-57---num
        #65-90---A-Z
        #97-122---a-z
        t=chr(s)
        re+=t
    return re