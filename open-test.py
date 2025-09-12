import csv
from os import system
import locale
from msvcrt import getwch
from time import sleep

feature = 0
current_features = [1, 2, 3, 4]

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
    system("cls")
    total_price = [0, 0]
    for idx, item in enumerate(products, 1):
        print(f"{idx}: {item["name"]}, {item["price"]}")
        total_price[0] += item["price"]
        total_price[1] += item["quantity"]
    print(f"total price: {int(total_price[0])}\ntotal quantity {total_price[1]}\navrage price: {int(total_price[0] / total_price[1])}")

def add():
    system("cls")
    print("product:")
    name = input("name:")
    desc = input("descritpion:")
    while True:
        try:
            price = float(input("price:"))
            break
        except:
            pass
    while True:
        try:
            quantity = int(input("descritpion:"))
            break
        except:
            pass
    temp_id = 0
    while True:
        if temp_id not in products["id"]:
            id = temp_id
            break
    return id, name, desc, price, quantity

while True:
    if feature == 1:
        products.pop(idx)

    elif feature == 2:
        system("cls")
        print(f'id: {products[idx]["id"]}\nname: "{products[idx]["name"]}"\nprice: {products[idx]["price"]}\ndescriotion: {products[idx]["desc"]}\nquantity: {products[idx]["quantity"]}\ntype to continue')
        sleep(1)
        temp = getwch()
        system("cls")

    elif feature == 3:
        id, name, desc, price, quantity = add()
        products.append(
            {                   
                "id": id,       
                "name": name,
                "desc": desc,
                "price": price,
                "quantity": quantity
            }
        )

    while True:
        list_products(products)
        while True:
            try:
                print("1 remove / 2 view / 3 add / 4 change: ")
                feature = int(getwch())
                if feature in current_features:
                    break
                else:
                    list_products(products)
            except:
                list_products(products)

        if feature != 3:
            while True:
                try:
                    idx = int(input(f"choose: ")) - 1
                    if 0 <= idx and idx <= len(products):
                        break
                    else:
                        list_products(products)
                        print("choose item within range of the list")
                except Exception as e:
                    list_products(products)
                    print("choose item within range of the list", e)
        break