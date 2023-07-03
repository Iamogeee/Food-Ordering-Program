print("STARBUCKS MENU\n")

StarbucksMenu = ['Iced Coffee', 'Blond Roast', 'Matcha Latte', 'Cold Brew', 'Caramel Macchiato', 'Pumpkin Spice Latte', 'Peppermint Mocha', 'Iced Green Lemonade', 'Mango Dragonfruit Refresher', 'Iced Dirty Chai Latte']

menu = enumerate(StarbucksMenu)

for ind, val in enumerate(StarbucksMenu):
  print(ind + 1, val)

order = []
request = (input("\nWhat would you like to order? (1 - 10): "))
choice = StarbucksMenu[int(request) - 1]
order.append(choice)
while True:
  add_request = (input("\nWhat else would you like to order? "))
  if add_request == "Done":
    break

  elif add_request.isnumeric and int(add_request) in range(1, 11):
    choice = StarbucksMenu[int(add_request) - 1]
    order.append(choice)
  
  
print("\nThank you for your order! Here is your order:")
for i in order:
  print(i)


if request in range(len(StarbucksMenu)):
  
  order.append(request)
  print(order)