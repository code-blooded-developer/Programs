def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]['bin']>currentvalue['bin']:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

   return alist

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]['bin']

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark]['bin'] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark]['bin'] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


tc = int(input())

while tc>0:
    tc -= 1
    n = int(input())

    arr = list(map(int, input().split()))

    obj = []
    for i in arr:
        obj.append({
            'val': i,
            'bin': bin(i).count('1')
        })

    insertionSort(obj)

    for i in obj:
        print(i['val'], end=' ')

    print()