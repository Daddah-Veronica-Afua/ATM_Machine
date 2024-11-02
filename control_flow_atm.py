from getpass import getpass

#Customer's balance
Balance = 1000000.00
pin = 1298

#Welcome message. The first message displayed on the ATM.
welcome = "Hello cherished customer, you are welcomed to PresVee Commercial Bank. We are at your service."
welcome += "\nKindly, insert your card in the slot."

#pin = int(getpass('Enter your PIN: '))

#Setting up the number of attempts
Number_of_attempts = 0

#Asking the customer to enter their pin
while Number_of_attempts < 3:
    Pin = int(input('Enter your PIN: '))
    if Pin == pin:
       break
    else:
        Number_of_attempts += 1
        print('PIN is incorrect. Try again.')
        if Number_of_attempts == 3:
            print('Too many incorrect attempts. Access blocked.')
            exit()



 
   


