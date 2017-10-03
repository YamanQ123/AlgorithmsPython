


def merge(a):
    aux = []
    mid = len(a)/2
    i = 0
    j = mid
    while i < mid and j < len(a):
        if a[i] < a[j]:
            aux.append(a[i])
            i += 1
        if a[j] < a[i]:
            aux.append(a[j])
            j +=1
        if a[i] == a[j]:
            aux.append(a[i])
            aux.append(a[j])
            i += 1
            j += 1
    while i < mid:
        aux.append(a[i])
        i += 1
    while j < len(a):
        aux.append(a[j])
        j += 1
    return aux


def merge( a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif b[j] < a[i]:
            c.append(b[j])
            j += 1
        elif a[i] == b[j]:
            c.append(a[i])
            c.append(b[j])
            i += 1
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


def sort(a):
    return sort(a,0,len(a))


def sort(a, start, end):
    if len(a) == 1:
        return a
    mid = end/2
    aux_1 = a[start:mid]
    aux_2 = a[mid:end]
    aux_1 = sort(aux_1,0,len(aux_1))
    aux_2 = sort(aux_2,0,len(aux_2))
    aux = merge(aux_1,aux_2)
    return aux

a = [1, 3, 5, 6, 2, 4, 8, 7]
e = [6 , 5 , 3 , 1 , 8 , 7 , 2 , 4]
f = ['alpha','cocacola',
     'statisfaction', 'beer',
     'british ','start up']
mid = len(a)/2
b = a[0:mid]
d = a[mid:len(a)]
print b
print d
c = merge(b,d)
print c
fz = sort(f,0,len(f))
print 'fz:',fz




