Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista = [1,2,3,4,5,6,7,8]
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8]
>>> lista.append(9)
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> max(lista)
9
>>> min(lista)
1
>>> len(lista)
9
>>> lista.sort()
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lista.reverse()
>>> lista
[9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> lista.extend([10,11])
>>> lista
[9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11]
>>> lista.remove(10)
>>> lista
[9, 8, 7, 6, 5, 4, 3, 2, 1, 11]
>>> lista(11)

>>> lista.remove(11)
>>> lista
[9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> lista
[9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> lista.insert(2,-3)
>>> lista
[9, 8, -3, 7, 6, 5, 4, 3, 2, 1]
>>> lista.sort()
>>> lista
[-3, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lista.remove(-3)
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lista.index(1)
0
>>> lista.pop()
9
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8]
>>> lista.append(9)
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>  lista([1,2,3,4,5,6,7,8,9])

>>> lista.count([1,2,3,4,5,6,7,8,9])
0
>>> y = [ a*10 for a in (lista)]
>>> y
[10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> for a in lista:
	print(a*10)

	
10
20
30
40
50
60
70
80
90
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> k= (lista[0:5])
>>> k
[1, 2, 3, 4, 5]
>>> u = (lista[5:])
>>> u
[6, 7, 8, 9]
>>> n = [[1,2,3],[4,5,6],[7,8,9]]
>>> n
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> n =[[1,2,3],[4,5,6],[7,8,9]]
flat=[]
for n in in nested:
        for m in n
        0=m
        flat,append(0)
>>> m = [1,2,3,4,5,6,7,8,9]
>>> m
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> m.append(n)
>>> 
>>> m = [1,2,3,4,5,6,7,8,9]
>>> m
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> n = [[1,2,3],[4,5,6],[7,8,9]]
>>> n
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> m.append(n)
>>> m
[1, 2, 3, 4, 5, 6, 7, 8, 9, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
>>> 
