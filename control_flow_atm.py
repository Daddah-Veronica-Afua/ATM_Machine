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

            def ATM_Menu():
                print("\nATM Menu:")
                print("1. Check Balance")
                print("2. Deposit Funds")
                print("3.Withdraw Funds")
                print("4. Change PIN")
                print("5. Exit")

                def Check_Balance():
                    print(f"Please your current balance is: {Balance}")

                    def Deposit_Funds():
                        Deposit = int(input("Enter amount to deposit: "))
                        if amount > 0:
                            balance += amount
                            print(f"{amount} deposited. New balance is: {balance}")
                            else:
                                print("Invalid amount. Please enter a positive number.")

                                def Change_Pin():
                                    current_pin = (input("Enter your PIN:"))
                                    if current_pin == pin:
                                        new_pin == int(input("Enter a new 4-digit PIN:"))
                                        confirm_pin = int(input("Confirm new PIN:"))
                                        if new_pin == confirm_new_pin:
                                            pin = new_pin
                                            print("PIN successfully changed.")
                                            else:
                                                print("PINs do not match.Try again.")
                                                else:
                                                    print("Incorrect current PIN.")



                    




 
   


