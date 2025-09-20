numero = int(input("Número:"))
cont = 1


"""
	while (cont<11):
	print ("%d * %d = %d" % (cont, numero, cont * numero))
	cont += 1
"""
for cont in range(1,11):
	print ("%2d * %d = %2d" % (cont, numero, cont * numero))