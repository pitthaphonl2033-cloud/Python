print("WELCOME TO MY SNACK SHOP")

print("<---------------------->")
print("1. M&Ms            $1.35")
print("2. Oreos           $2.46")
print("3. Nerds           $2.89")
print("4. Jolly Rancher   $3.29")
print("5. Skittles        $2.99")
print("6. Sour Patch Kids $4.29")
print("<---------------------->")

order=input("Order Menu (1-6)")
print("<--------------------------->")
price=0
if order =="1":
   print("You ordered M&Ms")
   price=1.35
elif order=="2":
     print("You ordered Oreos")
     price=2.46
elif order=="3":
     print("You ordered Nerds")
     price=2.89
elif order=="4":
     print("You ordered Jolly Rancher")
     price=3.29
elif order=="5":
     print("You ordered Skittles")
     price=2.99
elif order=="6": 
     print("You ordered Sour Patch Kids")
     price=4.29
else:
     print("Invalid Menu")

print("Total: $",price)

quantity=int(input("How many?"))
total = price * quantity
print("<----------------->")
print("Quantity:", quantity)
print("Total:$", total)

while True:
    print("Any more orders?")
    print("<---------------------->")
    print("1. M&Ms            $1.35")
    print("2. Oreos           $2.46")
    print("3. Nerds           $2.89")
    print("4. Jolly Rancher   $3.29")
    print("5. Skittles        $2.99")
    print("6. Sour Patch Kids $4.29")
    print("0. Checkout")
    print("<---------------------->")
    order=input("Order Menu")
    if order=="1":
        total += 1.35
        print("M&Ms added!")
    elif order=="2":
        total +=2.46
        print("Oreos added!")
    elif order=="3":
        total +=2.89
        print("Nerds added!")
    elif order=="4f":
        total +=3.29
        print("Jolly Rancher added!")
    elif order=="5":
        total +=2.99
        print("Skittles added!")
    elif order=="6":
        total +=4.29
        print("Sour Patch Kids added!")
    elif order=="0":
        break
else:
    print("Invalid Menu")
print("Total:$"), total

cash=int(input("Customer cash: "))

if cash >= total:
    change = cash-total
    print("Payment successful!")
    print("Change:$", change)
else:
    print("Not enough money!")



check=(input("Done? Press 0 Not yet? Press 1"))
   if check=="0":
       break
