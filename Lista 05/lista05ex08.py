print('='*50)
print('{:^50}'.format("Valores Iguais em duas Listas"))
print('='*50)
print()
N = int(input('Qual o Tamanho das lista?(Valor Inteiro): '))
listA = [' ']*N
listB = [' ']*N
print('\nLista A:\n')
for i in range(N):
	listA[i] = int(input('Valor {} da lista A: '.format(i+1)))
print('\nLista B:\n')
for i in range(N):
	listB[i] = int(input('Valor {} Lista B: '.format(i+1)))
cond = False
for i in range(N):
	for j in range(N):
		if listA[i] == listB[j]:
			cond = True
if cond == False:
	print('\nNão há valores repetidos!')
	cond = 'X'
if cond == True:
	print('\nExistem Valores Repetidos!!!\n')
	cond = 'X'