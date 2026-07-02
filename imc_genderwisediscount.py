print("SOME_SHOP")

customer_id = int(input("Enter your id            :"))
name = input("Enter your name          :")
gender = input("Enter your gender (f/m)  :")
price =  float(input("Enter your total price :"))

if gender == "f":
    if price > 5000:
        z = 0.05
    elif price > 4000 and price <= 5000:
        z = 0.04
    elif price <= 4000 and price > 2000:
        z = 0.03
    elif price <= 2000:
        z = 0.01
    else:
        print("NONE")
else:
    if price > 5000:
        z = 0.045
    elif price > 4000 and price <= 5000:
        z = 0.035
    elif price <= 4000 and price > 2000:
        z = 0.02
    elif price <= 2000:
        z = 0
    else:
        print("NONE")
discount_price = price * z
final_price = price- discount_price
print("----------------------------------------------------------")
print("YOUR RECIPT",)
print("----------------------------------------------------------")
print("discount_price :",discount_price)
print("----------------------------------------------------------")
print("final_price :",final_price)
print("----------------------------------------------------------")
print("                                                          ")
print("THANKYOU FOR SHOPPING!!! ,VISIT AGAIN!!!")


    
    
