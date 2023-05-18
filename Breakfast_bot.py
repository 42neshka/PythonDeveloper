milk = True
coffee = True
slicing = False
bred = False
curd_cheese = True
cucumber = True
tuna = False
salad = False
toasts = True
eggs = True
bacon = True
curd = True
sour_cream = False
banana = False
cheese = False

'''
def breakfast_def():
	for breakfast in range(5):
		if milk == 1:
			if milk and coffee == 1:
					print('У тебя на завтрак - Капучино')
					milk = milk - 1
		elif curd:
			print('Prog dont working')

breakfast_def()
'''

if milk and coffee:
	print('Капучино')
if toasts and tuna and curd_cheese and salad and cucumber:
	print('Тосты с тунцом и салатом')
elif toasts and tuna and curd_cheese and cucumber:
	print('Тосты с тунцом')
if banana and curd and sour_cream:
	print('Творог с бананом и сметаной')
if bacon and eggs and cheese:
	print('Яичница с сыром и беконом')
elif bacon and eggs:
	print('яичница с беконом')
if curd and eggs:
	print('Можно постараться и сделать сырники')
if bred and slicing and curd_cheese:
	print('Тосты с нарезками')