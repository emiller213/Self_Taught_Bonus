class Plane:
    money = 0
    first_class_tix_avail = 50
    business_class_tix_avail = 100
    economy_class_tix_avail = 200
    first_class_ticket_price = 500
    business_class_ticket_price = 400
    economy_class_tix_price = 300


class FirstClassPurchase:
    def __init__(self, quantity):
        self.quantity = quantity
        if Plane.first_class_tix_avail > 0:
            Plane.money += Plane.first_class_ticket_price
            Plane.first_class_tix_avail -= quantity
        else:
            print("Sorry, there are no more First Class Tickets Available.")


class BusinessClassPurchase:
    def __init__(self, quantity):
        self.quantity = quantity
        if Plane.business_class_tix_avail > 0:
            Plane.money += Plane.business_class_ticket_price
            Plane.business_class_tix_avail -= quantity
        else:
            print("Sorry, there are no more Business Class Tickets Available")


class EconomyClassPurchase:
    def __init__(self, quantity):
        self.quantity = quantity
        if Plane.economy_class_tix_avail > 0:
            Plane.money += Plane.economy_class_tix_price
            Plane.economy_class_tix_avail -= quantity
        else:
            print("Sorry, there are no more Economy Class Tickets Available")


FirstClassPurchase(10)
FirstClassPurchase(100)
FirstClassPurchase(50)
BusinessClassPurchase(10)
EconomyClassPurchase(100)


print("Hello, your plane has made $" + str(Plane.money))
