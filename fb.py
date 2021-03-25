def fizzbuzz(n: int):
	for i in range(1, n + 1):
		if i % 15 == 0:
			print('fizzbuzz')
		elif i % 5 == 0:
			print('buzz')
		elif i % 3 == 0:
			print('fizz')
		else:
			print(i)


if __name__ == '__main__':
	print('Input Number: ', end='')
	input_num = int(input())
	fizzbuzz(input_num)
