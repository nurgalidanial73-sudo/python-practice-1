customer_name = input("Enter customer name: ")
total = 0
items = 0
name=""
discount = 0
while(name != "done"):
    name = input("Enter item name (or 'done' to finish):")
    if(name != "done"):
        price = float(input("Enter price:"))
        total += price
        items+=1

period = int(input("Enter current hour(0-23):"))
if(period>=6 and period<12):
    print("Time period : Morning discount")
    discount = total*0.1
elif(period>=12 and period<17):
    print("Time period : No discount")
else:
    print("Time period : Evening discount")
    discount = total*0.05

total = total-discount

print("Customer: ",customer_name)
print("Items: ",items)
print("Discount: ",discount)
print("Tip(10%): ",total*0.1,"KZT")
print("Subtotal: ",total,"KZT")

print("Name uppercase: ", customer_name.upper())
print("Name lowercase: ", customer_name.lower())
print("Name length: ", len(customer_name))
if(customer_name[0].upper() == 'A' or customer_name[0].upper() == 'S' ):
    print("VIP customer")