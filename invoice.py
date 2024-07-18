# Import necessary modules
import datetime

# Define a class for items
class Item:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def total(self):
    return self.price * self.quantity

# Define a class for invoices
class Invoice:
  def __init__(self, customer_name, customer_address):
    self.customer_name = customer_name
    self.customer_address = customer_address
    self.items = []

  def add_item(self, item):
    self.items.append(item)

  def total(self):
    return sum(item.total() for item in self.items)

  def generate_invoice(self):
    invoice_number = "001"  # Replace with a unique invoice number
    date = datetime.date.today()

    print(f"Invoice #{invoice_number}")
    print(f"Customer: {self.customer_name}")
    print(f"Address: {self.customer_address}")
    print("Items:")
    for item in self.items:
      print(f"* {item.name} ({item.quantity}) - RS{item.price:.2f} each = RSSHIV{item.total():.2f}")
    print(f"Total: RS{self.total():.2f}")
    print(f"Date: {date}")

# Get user input
customer_name = input("Enter customer name: ")
customer_address = input("Enter customer address: ")

# Create an invoice object
invoice = Invoice(customer_name, customer_address)

# Get items from user
while True:
  item_name = input("Enter item name (or 'done' to finish): ")
  if item_name.lower() == 'done':
    break
  item_price = float(input("Enter item price: "))
  item_quantity = int(input("Enter item quantity: "))
  item = Item(item_name, item_price, item_quantity)
  invoice.add_item(item)

# Generate invoice
invoice.generate_invoice()