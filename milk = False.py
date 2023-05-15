milk = 1
coffee = 1
curd = True
sour_cream = True
banana = True


def breakfast_def():
	for breakfast in range(5):
		if milk == 1:
			if milk and coffee == 1:
					print('У тебя на завтрак - Капучино')
					milk = milk - 1
		elif curd:
			print('Prog dont working')

breakfast_def()