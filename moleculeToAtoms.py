def insertNum(f):
    i = 0
    while(i < len(f)):
        if f[i].isalpha():
            if i == len(f)-1:
                f = f + "1"
            elif not f[i+1].isnumeric()  and not f[i+1].islower():
                f = f[:i+1] + "1" + f[i+1:]
        elif f[i] == "]" or f[i] == ")" or f[i] == "}":
            if i == len(f) - 1:
                f = f + "1"
            elif not f[i+1].isnumeric():
                f = f[:i+1] + "1" + f[i+1:]
        i += 1
    return(f)

def getopp(s):
    if s == "(":
        return(")")
    elif s == "[":
        return("]")
    elif s == "{":
        return("}")

def getAtoms(f):
    i = 0
    while(i < len(f)):
        if f[i] == "(" or f[i] == "{" or f[i] == "[":
            t = getopp(f[i])
            j = i+1
            while f[j] != t:
                if f[j].isnumeric() and f[j-1].isalpha():
                    m = f[j]
                    x = j+1
                    while(f[x].isnumeric()):
                        m = m + f[x]
                        x = x+1
                    if(f[f.index(t)+1].isnumeric()):
                        f = f[:j] + str(int(m)*int(f[f.index(t)+1])) + f[j+len(m):]
                j += 1
            f = f[:i] + f[i+1:f.index(t)] + f[f.index(t)+2:]
            i = i-1
        i += 1
    return(f)
    
def parse_molecule (formula):
    f = insertNum(formula)
    f = getAtoms(f)
    d = {}
    (s,num) = ("", "")
    for i in range (len(f)):
        if f[i].isalpha():
            s += f[i]
        elif f[i].isnumeric():
            num += f[i]
            if(i == len(f)-1) or f[i+1].isalpha():
                d[s] = d.setdefault(s,0) + int(num)
                (s,num) = ("", "")
    return d

print(parse_molecule('K4[ON(SO3)2]2'))