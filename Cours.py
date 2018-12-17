#affichage d'un antislash
print "\\"

#Tableau Liste ou Tuple(en lecture seule)
MyListe = [var1,var2]
MyTuple = (var1,var2)

myShoppingList = ["Banane","Poireaux","Raclette","Caviar","Picon"]
myShoppingList.append["Poire"] #ajout un item
print myShoppingList(2)
print len(myShoppingList) # sera égale à 5
print myShoppingList[:2] # affiche les 2 premiers elements
print myShoppingList[:-1] # tout sauf le dennier
print myShoppingList[-1] # pop le dernier item du tableau

# parcour d'un tableau 
for produit in myShoppingList:
	print (produit)

i = 0 
while i <= len(myShoppingList)
	print myShoppingList[i]
	i= i + 1

# Dictionaire

User = {
	"Surname":"Mathey"
	"Name" : "Jérémy"
	"Age": 24
}

for u in User:
	print u

print User["Age"] # renvoie l'age soit 24 

User1 = {
	"Surname":"Lebris"
	"Name" : "M"
	"Age": 24
}

MyList = [User, User1]

print "Jérémy à " + str(MyList[0])


# un langage modulaire

#import os : bibliothèque de fonction de l'OS
#from time import sleep
#example : print os.system("Calc.exe")
#time.sleep(10)