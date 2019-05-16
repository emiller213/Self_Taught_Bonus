import csv

filename = 'inventory.csv'
with open(filename, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Identification Number", "Price", "Quantity on Hand"])
    writer.writeheader()


class Product:
    def __init__(self, identification_number, price, quantity_on_hand):
        self.identification_number = identification_number
        self.price = float(price)
        self.quantity_on_hand = quantity_on_hand

    def add_item(self):
        with open(filename, 'a', newline='') as csvFile:
            writer1 = csv.writer(csvFile)
            writer1.writerow([self.identification_number, self.price, self.quantity_on_hand])
            

Product(1, 1, 100).add_item()
Product(2, 200.09, 200).add_item()
Product(2, 3000.89, 200).add_item()
Product(2, 20.99, 200).add_item()
Product(2, 25.00, 200).add_item()
Product(2, 2.06, 200).add_item()
