import csv
import os
import locale

def format_currency(value):
    return locale.currency(value,grouping=True)


def load_data(filename): 
    products = []
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')

while True:
    os.system("cls")
    try:
        if feture == 1:
            print(products[choose])
        elif feture == 2:
            products.pop(choose)
    except:
        pass
    for idx, item in enumerate(products, 1):
        print(f"{idx}: {item["name"]}:")
    choose = int(input(f"choose 1 - {len(products)}: ")) - 1

    feture = int(input("1 remove, 2 view: "))