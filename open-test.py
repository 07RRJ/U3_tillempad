import csv
from os import system
import locale
from msvcrt import getwch

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

def list_products(products):
    for idx, item in enumerate(products, 1):
        print(f"{idx}: {item["name"]}:")

while True:
    system("cls")
    try:
        if feature == 1:
            products.pop(idx)

        elif feature == 2:
            print(f"{products[idx]}\ntype to continue")
            temp = getwch()
            system("cls")
    except:
        pass

    list_products(products)

    idx = int(input(f"choose: ")) - 1

    feature = int(input("1 remove / 2 view: "))