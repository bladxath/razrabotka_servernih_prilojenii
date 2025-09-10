class Product:
    def __init__(self, product_id, name, upc, manufacturer, price, shelf_life, amount):
        self.product_id = product_id
        self.name = name
        self.upc = upc
        self.manufacturer = manufacturer
        self.price = price
        self.shelf_life = shelf_life
        self.amount = amount

    def __repr__(self):
        return (f"Product(id={self.product_id}, name='{self.name}', upc='{self.upc}', "
                f"manufacturer='{self.manufacturer}', price={self.price}, "
                f"shelf_life={self.shelf_life} days, amount={self.amount})")

products = [
    Product(1, "Молоко", "0", "Молочник-Севаст", 150, 7, 42),
    Product(2, "Хлеб", "1", "Пекарь-Алушт", 80, 3, 37),
    Product(3, "Сыр", "2", "Молочник-Джанк", 200, 14, 22),
    Product(4, "Сок", "3", "Садовник-Бахчис", 200, 10, 20),
    Product(5, "Масло", "4", "Молочник-Саки", 300, 30, 12),
    Product(6, "Молоко", "5", "Молочник-Ялта", 150, 7, 19),
    Product(7, "Хлеб", "6", "Пекарь-Керчь", 80, 3, 87),
    Product(8, "Сыр", "7", "Молочник-Судак", 200, 14, 16),
    Product(9, "Сок", "8", "Садовник-Евпат", 200, 10, 54),
    Product(10, "Масло", "9", "Молочник-Симф", 300, 30, 25),
]

def find_products_by_name(name):
    return [product for product in products if product.name.lower() == name.lower()]

def find_products_by_name_and_price(name, max_price):
    return [product for product in products if product.name.lower() == name.lower() and product.price <= max_price]

def find_products_with_shelf_life_greater_than(min_shelf_life):
    return [product for product in products if product.shelf_life > min_shelf_life]

def find_products_by_amount(min_amount):
    return [product for product in products if product.amount >= min_amount]

print("Доступные продукты: ")
for product in products:
    print(product)

while True:
    print("\nВыберите фильтр (1-4):")
    print("1. По имени")
    print("2. По имени и цене")
    print("3. По сроку хранения")
    print("4. По количеству")
    print("5. Выход")
    
    choice = input("Введите ваш выбор: ")

    if choice == '1':
        name = input("Введите имя продукта: ")
        found_products = find_products_by_name(name)
        print("Отфильтрованный список продуктов:")
        for product in found_products:
            print(product)

    elif choice == '2':
        name = input("Введите имя продукта: ")
        max_price = float(input("Введите желаемую цену: "))
        found_products = find_products_by_name_and_price(name, max_price)
        print("Отфильтрованный список продуктов:")
        for product in found_products:
            print(product)

    elif choice == '3':
        min_shelf_life = int(input("Введите срок хранения продукта: "))
        found_products = find_products_with_shelf_life_greater_than(min_shelf_life)
        print("Отфильтрованный список продуктов:")
        for product in found_products:
            print(product)

    elif choice == '4':
        min_amount = int(input("Введите запрашиваемое количество: "))
        found_products = find_products_by_amount(min_amount)
        print("Отфильтрованный список продуктов:")
        for product in found_products:

            print(product)

    elif choice == '5':
        print("Выход из программы....")
        break

    else:
        print("Ошибка. Введите число от 1 до 5.")
