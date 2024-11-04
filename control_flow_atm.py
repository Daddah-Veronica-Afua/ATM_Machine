from getpass import getpass
#Customer's balance
Balance = 500
pin = None

#Welcome message. The first message displayed on the ATM.
welcome = "Hello cherished customer, you are welcomed to PresVee Commercial Bank. We are at your service."
welcome += "\nKindly, insert your card in the slot."
print(welcome)

#Customer's pin being set and saved for the first time.
if pin is None: 
    pin = getpass('Set your PIN: ') 
print('PIN set successfully.')


#Setting up the number of attempts
Number_of_attempts = 0

#Asking the customer to enter their pin
while Number_of_attempts < 3:
    entered_pin = getpass('Enter your PIN: ') 
    if entered_pin == pin: 
        break
    else:
        Number_of_attempts += 1
        print('PIN is incorrect. Try again.')
        if Number_of_attempts == 3:
            print('Too many incorrect attempts. Access blocked.')
            exit()

#Displaying main menu
def ATM_menu():
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Funds")
    print("3. WithdrawalFunds")
    print("4. Change PIN")
    print("5. Exit")


#Checking Balance
def Check_Balance(): 
    print(f"Your current balance is: GHS {Balance:.2f}") 

#Depositing funds
def Deposit_Funds(): 
    global Balance, total_deposit
    Deposit = float(input("Enter amount to deposit: ")) 
    if Deposit > 0: 
        Balance += Deposit 
        total_deposit += Deposit
        print(f"GHS {Deposit:.2f} deposited. New balance is: GHS {Balance:.2f}") 
    else: print("Invalid amount. Please enter a positive number.") 
total_deposit = 0
total_withdrawal = 0

#Withdrawing funds
def Withdraw_Funds(): 
    global Balance, total_withdrawal 
    Withdrawal= float(input("Enter amount to withdraw: ")) 
    if Withdrawal> 0: 
        if Withdrawal<= Balance: 
            Balance -= Withdrawal
            total_withdrawal += Withdrawal
            print(f"GHS {Withdrawal:.2f} withdrawn. New balance is: GHS {Balance:.2f}") 
        else: print("Insufficient funds. Cannot Withdrawalmore than your balance.") 
    else: print("Invalid amount. Please enter a positive number.") 
    
#Change pin    
def Change_Pin(): 
    global pin 
    current_pin = getpass("Enter your current PIN:") 
    if current_pin == pin: 
        new_pin = getpass("Enter a new 4-digit PIN:") 
        confirm_new_pin = getpass("Confirm new PIN:") 
        if new_pin == confirm_new_pin: 
            pin = new_pin 
            print("PIN successfully changed.") 
        else: print("PINs do not match. Try again.") 
    else: print("Incorrect current PIN.")

#Setting up choices for the Main Menu
while True: 
    ATM_menu() 
    choice = int(input("Select a transaction: ")) 
    if choice == 1: 
        Check_Balance() 
    elif choice == 2: 
       Deposit_Funds() 
    elif choice == 3: 
        
       Withdraw_Funds() 
    elif choice == 4: 
        Change_Pin() 
    elif choice == 5: 
        print(f'Thank you for using PresVee ATM. Here is a summary of your transactions: \nTotal amount deposited : GHS {total_deposit}. \nAmounts withdrawn : GHS {total_withdrawal}') 
        print("Goodbye!")
        break 
    else: 
      print("Invalid option. Please select again.")

