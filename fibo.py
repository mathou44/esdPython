"""
Ce super programme realise une magnifique suite de fibonnacci de taille defini par l'utilisateur
"""


NumIte = input("Merci de saisir la taille de la suite a afficher : ")


def fibo(Taille):
		num1 = 1
		num2 = 1
		temp = 0
		i = 1
		while i < int(Taille+1):
			temp = num1 + num2
			num1 = num2
			num2 = temp
			i = i+num1 
			print(num1)

fibo(NumIte)