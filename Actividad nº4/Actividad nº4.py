#Item 1
import pdb
pdb.set_trace()

listas=[[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
maximo=[max(x)for x in listas]
print(maximo)

#Item 2
def es_primo(n):
    primo = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    return primo

lista1= [3, 4, 8, 5, 5, 22, 13]
primos= list(filter(es_primo,lista1))
print(primos)