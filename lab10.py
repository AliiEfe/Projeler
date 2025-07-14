# class Instrument:
#     def playSound(self):
#         print("Some generic instrument sound")
#
# class Guitar(Instrument):
#     def playSound(self):
#         print("Strum")
#
# class Drum(Instrument):
#     def playSound(self):
#         print("Boom")
#
# def main():
#     instruments = [Guitar(), Drum()]
#     for instrument in instruments:
#         instrument.playSound()
#
#
# if __name__ == "__main__":
#     main()



# class Vehicle:
#     def displaySpeed(self):
#         print("Speed not defined")
#
# class Car(Vehicle):
#     def displaySpeed(self):
#         print("Car speed: 120 km/h")
#
#
# class Bicycle(Vehicle):
#     def displaySpeed(self):
#         print("Bicycle speed: 25 km/h")
#
#
# def main():
#     vehicles = [Car(), Bicycle()]
#     for v in vehicles:
#         v.displaySpeed()
#
#
# if __name__ == "__main__":
#     main()



# class Item:
#     def applyDiscounts(self, prices):
#         print("Applying discounts.")
#
# class Electronics(Item):
#     def applyDiscounts(self, prices):
#         print("Electronics:")
#         for price in prices:
#             discounted = price * 0.90
#             print(f"Original price: {price}, Discounted price: {discounted}")
#
#
# class Clothing:
#     def applyDiscounts(self, prices):
#         print("Clothing:")
#         for price in prices:
#             discounted = price * 0.80
#             print(f"Original price: {price}, Discounted price: {discounted}")
#
#
# def main():
#     items = [Electronics(), Clothing()]
#     electronic_prices = [100.0, 150.0]
#     clothing_prices = [80.0, 120.0]
#
#     items[0].applyDiscounts(electronic_prices)
#     items[1].applyDiscounts(clothing_prices)
#
# if __name__ == "__main__":
#     main()




# class Payment:
#     def processPayment(self):
#         print("Processing payment.")
#
#
# class CreditCardPayment(Payment):
#     def processPayment(self):
#         print("Processing credit card payment.")
#
#
# class PayPalPayment(Payment):
#     def processPayment(self):
#         print("Processing PayPal payment.")
#
#
# def main():
#     payments = [CreditCardPayment(), PayPalPayment()]
#     for p in payments:
#         p.processPayment()
#
#
# if __name__ == "__main__":
#     main()

