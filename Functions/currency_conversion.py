# WAF to convert USD to INR.

def conversion(indian):
    
    if indian == 0 or indian == None:
        return 1
    else:
        return indian*85.71
    
indian = int(input("Enter The Amount in USD: "))

print("The vale of $"f"{indian} is ₹", conversion(indian),"Indian Rupee")

#for INR to USD

def inr_usd(usd):
    
    if usd == 0 or usd == None:
        return 1
    else:
        return usd*0.012
    

usd = float(input("Enter The Amount in INR: "))

print("The Vale of ₹ "f"{usd} is $", inr_usd(usd))
