from Dictionaries.Functions import *
usuarios={}
opcao= question()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
	 if opcao=="I":
		insert(usuarios)
	 opcao = question()