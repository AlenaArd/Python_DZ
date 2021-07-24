"""
print('Давайте создадим структуру данных «Товары»')
n = int(input('Введите колличество товаров '))
i = 1
products = {
	'название': 'товар',
	'цена (руб)': 0.01,
	'кол-во товра (ед.)': 1,
	'комлектация товара (шт.)': 1
}
products_el = []
good = []
products_st =[]
while i <= n:
	products['название'] = input('Введите товар - '),
	products['цена (руб)'] = float(input('Введите цену товара -  ')),
	products['кол-во товра (ед.)'] = int(input('Введите кол-во товара -  ')),
	products['комлектация товара (шт.)'] = int(input('Введите комлектация товара (шт.) -  '))
	np = i
	products_el.append(np)
	products_el.append(products)
	good = tuple(products_el)
	products_st += good
	i += 1
else:
	print('Давайте помотрим структуру данных «Товары»:')
	print(products_st)

# ВВод данных работает c ошибкой, сохранила до лучших времен для себя

"""

products_st = [
	(1, {'название': 'учебники для 5 класса', 'цена (руб.коп)' : '101.12', 'кол-во товра (ед.)': '5', 'комлектация товара (шт.)': '8'}),
	(2, {'название': 'учебники для 6 класса', 'цена (руб.коп)' : '123.20', 'кол-во товра (ед.)': '13', 'комлектация товара (шт.)': '11'}),
	(3, {'название': 'учебники для 7 класса', 'цена (руб.коп)' : '140.55', 'кол-во товра (ед.)': '7', 'комлектация товара (шт.)': '10'})
]
product_list = {}
for i, product in products_st:
	for key, value in product.items():
		if not product_list.get(key):
			product_list[key] = [value]
		else: product_list[key].append(value)
print(product_list)
