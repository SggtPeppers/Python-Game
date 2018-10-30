
print(" _______")
print("|       |")
print("|")
print("|")
print("|")
print("|")
print("⟘")
print("\n")
import random
import os

palabras = ["casa","caballo","cigarrillo","celular","mesa","computadora","casco","botella",
"multiplo","control","distrofia","artritis","cuadriplejia","ligamento","orina","pantorrilla",
"trasladar","vejiga","velcro","television","escenario","alcahuete","ebullicion","hostigar",
"descenso","embarcar","escabullirse","fehaciente","golpiza","habitaculo","halagar","hazmerreir",
"hectarea","hechicero","hemorragia","herbivoro","heroismo","hojalata","homicida","honestidad",
"ahorcado","hornero","hospedaje","huracan","impaciencia","incineracion","incorruptible",]

guess_word = []
duration = 0.5
freq = 800
key_word = random.choice(palabras)
length_word = len(key_word)


alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

def print_word_to_guess(letters):
	print("⹅"*length_word*3)	
	print(" ".join(letters))
	print("⹅"*length_word*3)
def change():
	for character in key_word:
		guess_word.append("_ ")
	print("Well, the word You need to guess has", length_word, "characters")
	print("Be aware that You can enter only 1 letter form a-z")
	print_word_to_guess(guess_word)



def guessing():

	turn=7

	while turn > 0 : 
		guess = input("Choose a Letter: ").lower()
		
		if not guess in alphabet:
			print("\n")
			print("⹅"*34)			
			print("Enter just one letter from a-z alphabet")
			print("⹅"*34)
			print("\n")
		elif guess in letter_storage:
			print("\n")
			print("⹅"*34)			
			print("You already guessed that letter!!")
			print("⹅"*34)
			print("\n")	

		else:
			letter_storage.append(guess)
			if guess in key_word:
				print("\n")				
				print("You guessed correctly!")
				for x in range(0,length_word):
					if key_word[x] == guess:
						guess_word[x] = guess
				print("\n")
						
				print_word_to_guess(guess_word)
				

				if not "_ " in guess_word:
					print("\n")					
					print("You Won!!")
					print("\n")					
					print("Game Over")
					break

			else:
				print("\n")
				print("The letter is not in the word. Try Again!")
				
				turn = turn - 1
				if turn == 6:
					print("\n")
					print(" _______")
					print("|       |")
					print("|      ☹")
					print("|")
					print("|")
					print("|")
					print("⟘")
					print_word_to_guess(guess_word)				
				elif turn == 5:
					print("\n")
					print(" _______")
					print("|       |")
					print("|      ☹")
					print("|       | ")
					print("|")
					print("|")
					print("⟘")
					print_word_to_guess(guess_word)
				elif turn == 4:
					print("\n")
					print(" _______")
					print("|       |")
					print("|      ☹")
					print("|      /|")
					print("|")
					print("|")
					print("⟘")
					print_word_to_guess(guess_word)
				elif turn == 3:
					print("\n")
					print(" _______")
					print("|       |")
					print("|      ☹")
					print("|      /|\ ")
					print("|")
					print("|")
					print("⟘")
					print_word_to_guess(guess_word)
				elif turn == 2:
					print("\n")
					print(" _______")
					print("|       |")
					print("|      ☹")
					print("|      /|\ ")
					print("|       |")
					print("|")
					print("⟘")
					print_word_to_guess(guess_word)
				elif turn == 1:
					print("\n")
					print(" _______")
					print("|       |")
					print("|      ☹")
					print("|      /|\ ")
					print("|       |")
					print("|      /")
					print("⟘")
					print_word_to_guess(guess_word)

				elif turn == 0:
					print("\n")
					print(" _______")
					print("|       |")
					print("|      ☹")
					print("|      /|\ ")
					print("|       |")
					print("|      / \ ")
					print("⟘")
					print("\n")
					print(" Sorry Mate, You lost :<! The secret word was",key_word)
					

change()
guessing()
	













