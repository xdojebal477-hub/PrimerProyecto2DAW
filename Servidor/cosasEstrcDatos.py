lista=[1,2,3,4,5]
print(lista)
print(type(lista))
print(len(lista)) # longitud de la lista
lista.sort(reverse=True) # ordena la lista en reversa (modifica la original)
print(lista)
#--------------------------------------------------------------------
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))

print(list(enumerate(seasons, start=1)))