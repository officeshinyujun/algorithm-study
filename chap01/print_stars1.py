print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(n):
	print('*', end = '' )
	if  (i+1) % 5 == 0:
		print()
print() 

