#Enter the price of the House you wish to Buy
print("Enter the house price")
price = float(input())

#Enter the first name
print("Enter the first name:")
first_name = input()

#Enter the last name
print("Enter the last name:")

#Enter spouse's or partner's first and last name
last_name = input()
print("Enter spouse's or partner's first name: ")
p_first_name = input()
print("Enter spouse's or partner's last name: ")
p_last_name = input()

#Enter the email
print("Enter email: ")
email = input()

#Enter the phone number
print("Enter the phone number: ")
phone = input()

#Enter the mailing address
print("Enter the mailing address: ")
address = input()

#Enter city
print("Enter the City: ")
city = input()

#Enter State
print("Enter the State: ")
state = input()

#Enter zip code
print("Enter the zip code: ")
zipcode = input()

#Added CreditScore variable
print("Enter the client's credit score: ")
CreditScore = int(input())

# initializing variables
fullname = first_name + " " + last_name
partner_name = p_first_name + " " + p_last_name
credit_status = ""
downPayment = 0

# making a decision about the down-payment payable using if-else

if 780 <= CreditScore <= 850:
    credit_status = "Excellent Credit"
    downPayment = 0.10 * price
elif 740 <= CreditScore <= 779:
    credit_status = "Very Good"
    downPayment = 0.1 * price
elif 720 <= CreditScore <= 739:
    credit_status = "Above Average"
    downPayment = 0.3 * price
elif 680 <= CreditScore <= 719:
    credit_status = "Average"
    downPayment = 0.6 * price
elif 620 <= CreditScore <= 679:
    credit_status = "Below Average"
    downPayment = 0.18 * price
elif 580 <= CreditScore <= 619:
    credit_status = "Poor Credit Score"
    downPayment = 0.20 * price
elif CreditScore < 520:
    credit_status = "Poor Credit Score"
    downPayment = 0.25 * price

print()
print("Name: " + fullname)
print("Physical Address: " + address)
print("City: " + city + " State: " + state + " Zipcode: " + zipcode)
print()
print("New House Price: ${:,.2f}".format(price))
print("Downpayment: ${:,.2f}".format(downPayment))
print("Credit Score: " + str(CreditScore))
print("Credit Status: " + credit_status)
print()
print("CONGRATULATIONS - YOU NOW OWN YOUR DREAM HOME - " + fullname + " and " + partner_name)