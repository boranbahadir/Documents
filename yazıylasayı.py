import time

birler = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayı):
	birinci = sayı % 10
	ikinci = sayı // 10

	return onlar[ikinci] + " " + birler[birinci]

print("Çıkmak için q ")
while True:
	sayı = input("Sayı:")
	if sayı == "q":
		time.sleep(1)
		print("Güle güle")
		break

	else:	
		sayı = int(sayı)
		print(okunus(sayı))
