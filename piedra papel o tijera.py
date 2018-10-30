

import random as r

list = ["Piedra", "Papel", "Tijera"]

x = r.choice(list)


def ppt(y):
	if y == list[0] and x == list[0]:
		print("Tie!! Play again!")
	if y == list[0] and x == list[1]:
		print("You Lost!!")
	if y == list[0] and x == list[2]:
		print("You Win!!")

	if y == list[1] and x == list[1]:
		print("Tie!! Play again!")
	if y == list[1] and x == list[2]:
		print("You Lost!!")
	if y == list[1] and x == list[0]:
		print("You Win!!")

	if y == list[2] and x == list[2]:
		print("Tie!! Play again!")
	if y == list[2] and x == list[0]:
		print("You Lost!!")
	if y == list[2] and x == list[1]:
		print("You Win!!")

print()
ppt(input("Elige Piedra, Papel o Tijera: "))
print()
print("La Computadora eligio: ", x)
print()




