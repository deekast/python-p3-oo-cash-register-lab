#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
  
  def add_item(self, title, price, quantity = 1):
    self.total += (price * quantity)
    self.last_transaction = {
      "title": title,
      'price': price,
      'quantity': quantity

    }
    for _ in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    if self.discount == 0:
      print ("There is no discount to apply.")
    else:
      self.total = self.total - (self.total * (self.discount / 100))
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    for _ in range(self.last_transaction.get('quantity')):
      self.total -= self.last_transaction.get('price')