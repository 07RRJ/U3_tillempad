import csv, locale
from os import system
from msvcrt import getwch
from time import sleep

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


def list_products(products):
    system("cls")
    total_price = [0, 0]
    print(f"|{"=" * 6}|{"=" * 26}|{"=" * 63}|{"=" * 9}|{"=" * 5}|")
    print(f"|  Id  | {"=" * 9} Name {"=" * 9} | {"=" * 24} Description {"=" * 24} |  Price  | Qty |")
    print(f"|{"=" * 6}|{"=" * 26}|{"=" * 63}|{"=" * 9}|{"=" * 5}|")
    for idx, item in enumerate(products, 1):
        name_display = item["name"][:21] + "..." if len(item["name"]) > 24 else item["name"]
        desc_display = item["desc"][:57] + "..." if len(item["desc"]) > 60 else item["desc"]
        print(f"|{idx:>4}:   {name_display:<27} {desc_display:<60}   {item['price']:<7}   {item["quantity"]:<4}|")
        total_price[0] += item["price"]
        total_price[1] += item["quantity"]
    print(f"|{"=" * size}|")
    print(f"| {f"total price: {int(total_price[0])}":35} | {f"total quantity: {total_price[1]}":35} | {f"avrage price: {int(total_price[0] / total_price[1])}":35} |")
    print(f"|{"=" * size}|")

def name_product(idx):
    system("cls")
    print(f'id: {products[idx]["id"]}\nname: "{products[idx]["name"]}"\nprice: {products[idx]["price"]}\ndescriotion: {products[idx]["desc"]}\nquantity: {products[idx]["quantity"]}\ntype to continue')
    sleep(1)
    temp = getwch()
    system("cls")

def add():
    system("cls")
    print("new product:")
    name = input("name: ")
    desc = input("description: ")
    while True:
        try:
            price = float(input("price: "))
            break
        except:
            pass
    
    while True:
        try:
            quantity = int(input("quantity: "))
            break
        except:
            pass
    
    ids = []
    for item in products:
        ids.append(item["id"])
    new_id = max(ids) + 1

    return {                   
        "id": new_id,       
        "name": name,
        "desc": desc,
        "price": price,
        "quantity": quantity
    }

def change(idx):
    system("cls")
    print(f'|{"=" * size}|')
    print(f'| {f"changing item: {idx + 1}, id: {products[idx]["id"]}":111} | \n|{"=" * size}|\n| {f'name: "{products[idx]["name"]}"':111} |\n| {f'descriotion: {products[idx]["desc"]}':111} |\n| {f'price: {products[idx]["price"]}':111} |\n| {f'quantity: {products[idx]["quantity"]}':111} |\n|{"=" * size}|')
    print("leave empty to skipp")

    change_item = products[idx]

    name = input("name: ")
    desc = input("description: ")

    while True:
        price = input("price: ")
        if price == "":
            change_item["price"] = products[idx]["price"]
            break
        try:
            change_item["price"] = float(price)
            break
        except Exception as e:
            print(e)

    while True:
        quantity = input("quantity: ")
        if quantity == "":
            change_item["quantity"] = products[idx]["quantity"]
            break
        try:
            change_item["price"] = int(quantity)
            break
        except:
            pass

    if not name:
        change_item["name"] = products[idx]["name"]
    else:
        change_item["name"] = name
    if not desc:
        change_item["desc"] = products[idx]["desc"]
    else:
        change_item["desc"] = desc

    return change_item

def save(products):
    with open('save.csv', 'w', newline='') as f:
        fieldnames = ['id', 'name', 'desc', 'price', 'quantity']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  
feature = 0
current_features = ["r", "v", "a", "c", "q"]
size = 113
products = load_data('db_products.csv')

while True:
    if feature == "r":
        products.pop(idx)

    elif feature == "v":
        name_product(idx)

    elif feature == "a":
        products.append(add())

    elif feature == "c":
        products[idx] = change(idx)
    
    elif feature == "q":
        save(products)
        break

    while True:
        list_products(products)
        while True:
            try:
                print("(R)emove / (V)iew / (A)dd / (C)hange / (Q)uit: ")
                feature = getwch().lower()
                if feature in current_features:
                    break
                else:
                    list_products(products)
            except:
                list_products(products)

        if feature not in ["a", "q"]:
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