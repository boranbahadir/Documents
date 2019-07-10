liste = ["555","cvcv","213dfd","13gfg","sdsdsd22"]

for i in liste:
	try:
		print("Bu değer sayı",int(i))
	except ValueError:
		print("Bu değer sayı değil",i)

