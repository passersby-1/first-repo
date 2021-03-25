def fizzbuzz(n: int):
	for i in range(1, n + 1):
		if i % 15 == 0:
			print('fizzbuzz')


if __name__ == '__main__':
	fizzbuzz(15)
