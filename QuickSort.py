def exchange(i, j, a):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def partition(start,end,a):
    i = start
    wall = start
    pivot = end - 1
    while i < pivot:
        if a[i] < a[pivot]:
            #print 'a[i]: ',a[i],'< a[pivot]: ',a[pivot],"exchanging"
            exchange(i, wall, a)
            wall += 1
            i += 1
            #print i
        else:
            i += 1
            #print i
    exchange(wall, pivot, a)
    return wall


def sort(start,end,a):
    if end - start == 1 or end == start:
        return
    else:
        wall = partition(start, end, a)
        sort(start, wall, a)
        sort(wall+1, end, a)



e = [6 , 5 , 24,124,23,4,12,4,3244,23,2,3,2,3,2,4,23,4,32,2,3,4,12,41,24,32,4,23,324,324,23,4,34,3,4,34,34,3,43,43,43,23,2,42,4,1,24,324,32,41,4,32,432
     ,234234,2,3,4,3,2,4,23,4,324,23,4,324,32,4,324,32,423,4,324,32,4,324,1,54,656,867867,85,7,456,35,576,5,5,235,547,56,45,412,423,45,6756,865,435,6,573 , 1 , 8 , 7 , 2 , 4,123,32,5423,512,412,5,124,124,23,5,1,45,23]
sort(0,len(e),e)
print e
