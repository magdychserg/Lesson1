product_dict = {'name': None,
                'price': None,
                'quantity': None,
                'unit': None}

analitic = {'name': [],
             'price': [],
             'quantity': [],
             'unit': []}
new_product = []
i = 0
while True:
    continue_check = input("Continue enter products (Yes-1, No-0, Analitics- 2): ")
    if continue_check == '0':
        print(f'Today product added: {new_product}')
        break
    elif continue_check == '2':
        for key, value in analitic.items():
            print(f'{key}: {value}')
        break
    i += 1
    product_dict['name'] = input("Enter the product name: ")
    product_dict['price'] = int(input("Enter price: "))
    product_dict['quantity'] = int(input("Enter quantity: "))
    product_dict['unit'] = input("Enter unit: ")
    new_product.append((i, product_dict.copy()))
    for f in product_dict:
        analitic[f].append(product_dict[f])

