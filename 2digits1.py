print ('2자리 양수를 입력하세요.')

while True:
	no = int (input('값을 입력하세요.:'))
	if no > 9 and no < 100:
		break

print (f'입력받은 양수는 {no}입니다.')
