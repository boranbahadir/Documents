import math
import sys

def secim(k):
	print("""MATHMATMHMATMAHMATMAHMAHMATMAHM
Toplama için 1
Çıkarma için 2
Çarpma için 3
Bölmek için 4
Faktoriyel için 5
Büyüye yuvarlamak için 6
Küçüğe yuvarlamak için 7
-----------------
Çıkmak için Q
Program esnasında bu menüye ulaşmak için \"geri\" yazınız.
MATMAHMATMAHMATMHMATHMATMHMAHMMA
""")

	k = input()

	if k == "1": 	
		while True:
			(toplama(1,2))
	elif k == "2":
		while True:
			(cikar(1,2))
	elif k == "3":
		while True:
			(çarpma(1,2))
	elif k == "4":
		while True:
			(bol(4,3))

	elif k == "5":
		while True:
			(faktoriyel(4))

	elif k == "6":
		while True:
			(buyuk_yuvarla(1))

	elif k == "7":
		while True:
			(kucuk_yuvarla(1))

	elif k == "q" or k == "Q":
		sys.exit("Çıkılıyor")

#----------------------------------------------


def toplama(a,b):
	# iki sayıyı toplar
	a = input("İlk sayı:")
	if a == "geri":
		secim(1)
	else:
		b = input("İkinci Sayı:")
		a = int(a)
		b = int(b)
		print("{} + {} = {}".format(a,b,a+b))

#----------------------------------------------

def çarpma(a,b):
	# iki sayıyı çarpar
	a = input("İlk sayı:")
	if a == "geri":
		secim(1)
	else:
		b = input("ikinci sayı:")
		a = int(a)
		b = int(b)
		print("{} * {} = {}".format(a,b,a*b))

#----------------------------------------------

def bol(a,b):
	# iki sayıyı böler
	a = input("İlk sayı:")
	if a == "geri":
		secim(1)
	else:
		b = input("İkinci Sayı:")
		a = int(a)
		b = int(b)
		print("{} / {} = {}".format(a,b,a/b))

#----------------------------------------------

def cikar(a,b):
	# iki sayıyı çıkarır
	a = input("İlk sayı:")
	if a == "geri":
		secim(1)
	else:
		b = input("İkinci Sayı:")
		a = int(a)
		b = int(b)
		print("{} - {} = {}".format(a,b,a-b))

#----------------------------------------------


def faktoriyel(sayı):
	#sayının faktoriyelini bulan fonksiyon
	sayı = input("Sayı:")
	if sayı == "geri":
		secim(1)
	else:
		sayı = float(sayı)
		print("Girdiğin sayının faktoriyeli.",math.factorial(sayı))

#----------------------------------------------

def kucuk_yuvarla(a):
	# float girilen sayıyı en küçüğe yuvarlar
	a = float(input("Sayı:"))
	if a == "geri":
		secim(1)
	else:
		print("Küçüğe Yuvarlanmış hali:",math.floor(a))

#----------------------------------------------

def buyuk_yuvarla(a):
	# float girilen sayıyı en küçüğe yuvarlar
	a = float(input("Sayı:"))
	if a == "geri":
		secim(1)
	else:
		print("Büyüğe Yuvarlanmış hali:",math.ceil(a))

#----------------------------------------------

secim(1)
