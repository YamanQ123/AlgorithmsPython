# import webbrowser
# import time
# i=1
# print 'the probram has started ',time.ctime()
# while i>0:
#     time.sleep(1)
#     webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     i-=1

id = [1, 1, 1, 8, 3, 0, 5, 2, 8, 4]


def root_of(p):
    while id[p] != p:
        p = id[p]
    return p


def union(p, q):
    root_p = root_of(p)
    root_q = root_of(q)
    id[root_p] = root_q


print root_of(6)
union(4, 7)
print id