# -*- coding: utf-8 -*-

def enpl():
	dictionary = {}
	with open("madness-and-oppression-dictionary.txt", "r") as file:
		for line in file:
			key, value = line.strip().split(" - ")
			dictionary[key] = value
			if (en.lower() in key.lower()):
				print(key+" - "+value)
	print("")
	return


def plen():
	dictionary = {}
	with open("madness-and-oppression-dictionary.txt", "r") as file:
		for line in file:
			value, key = line.strip().split(" - ")
			dictionary[key] = value
			if (pl.lower() in key.lower()):
				print(key+" - "+value)
	print("")
	return


slownik = input("angielski -> polski (1)\npolski -> angielski (2)\nWybierz słownik: ")
print("Wyjście: /\n")
if (slownik == 1):
	en = str(raw_input("Podaj angielskie słowo: "))
	print("")
	enpl()
	while (en!="/"):
		en = str(raw_input("Podaj angielskie słowo: "))
		print("")
		enpl()
elif (slownik == 2):
	pl = str(raw_input("Podaj polskie słowo: "))
	print("")
	plen()
	while (pl!="/"):
		pl = str(raw_input("Podaj polskie słowo: "))
		print("")
		plen()
