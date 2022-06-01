import random
import datetime
from customer import Customer

atm = Customer(id)

#Checking
while True : 
    id = int(input("Enter your PIN number here: \n"))
    trial = 0 

    while (id != int(atm.checkPin()) and trial<3) :
        id = int(input("Incorrect PIN number, try again: \n"))
        trial+=1 
        if trial==3 :
            print("ATM BLOCKED!\nWe cannot process your transaction, please contact our customer service.")
            exit()
    
    #Main Looping
    while (id == int(atm.checkPin())) :
        print("                 IMC BANK             ")
        print("          Your Financial Solution     ")
        print("--------------------------------------")
        print("\nSELECT TRANSACTION \n1 - Check Balance \t4 - Change PIN Number \n2 - Withdrawal \t5 - Other \n3 - Deposit") 
        choosing_menu = int(input("What would you like to do?\n"))
        if choosing_menu==1 : #Check Balance
            print(f"Balance Information \nRp {atm.checkBalance()}")
            next_transaction_menu_1 = int(input("Do you want to do another transaction? \n1. YES \t2. NO \n"))
            if next_transaction_menu_1==1:
                choosing_menu
            else :
                print("Please take your ATM Card")
                exit()
        elif choosing_menu==2 : #Withdrawal Transaction
            withdrawal_nominal = int(input("Input nominal for your withdrawal:\nRp "))
            verif_withdrawal_transaction = int(input(f"Are you sure to continue this transaction? Rp {withdrawal_nominal}? \n1 - CONTINUE \t2 - CANCEL \n"))
            if verif_withdrawal_transaction==1 and withdrawal_nominal<atm.checkBalance():
                atm.withdrawBalance(withdrawal_nominal)
                print(f"Transaction Successful! \nBalance Information: Rp {atm.checkBalance()}")
                next_transaction_menu_2_1 = int(input("Do you want to do another transaction? \n1. YES \t2. NO \n"))
                if next_transaction_menu_2_1==1 :
                    choosing_menu
                else :
                    exit()
            else :
                print(f"You have not enough balance to process this transaction. Your Balance is Rp {atm.checkBalance()}")
                next_transaction_menu_2_2 = int(input("Do you want to do another transaction? \n1. YES \t2. NO \n"))
                if next_transaction_menu_2_2==1 :
                    choosing_menu
                else :
                    print("Please take your ATM Card")
                    exit()
        elif choosing_menu==3 : #Deposit Transaction
            deposit_nominal = int(input("Input nominal for your deposit :\nRp "))
            verif_deposit_transaction = int(input(f"Are you sure to continue this transaction Rp {deposit_nominal}? \n1. CONTINUE \t2. CANCEL \n"))
            if verif_deposit_transaction==1 :
                atm.depositBalance(deposit_nominal)
                print(f"Transaction Successful! \nBalance Information Rp {atm.checkBalance()}")
                next_transaction_menu_3_1 = int(input("Do you want to do another transaction? \n1. YES \t2. NO \n"))
                if next_transaction_menu_3_1==1 :
                    choosing_menu
                else :
                    print("Please take your ATM Card")
                    exit() 
        elif choosing_menu==4 : #Change PIN number
            while True :
                pin_verification = int(input("Input your PIN number :\n"))
                trial=0        
                while (pin_verification != int(atm.checkPin()) and trial<3): #Looping for old pin verification
                    print("Incorrect PIN, please try again.")
                    pin_verification = int(input("Input your PIN number :\n"))
                    trial+=1
                    if trial==3 :
                        print("ATM BLOCKED!\nWe cannot process your transaction, please contact our customer service.")
                        exit()
                while (pin_verification == int(atm.checkPin())):    #Looping for new pin verification  
                    update_pin = int(input("Input your new PIN number: \n"))
                    verify_new_pin = int(input("Input your new PIN number again: \n"))
                    trial_new_pin = 0
                    while (verify_new_pin != update_pin and trial_new_pin<3):
                        print("Incorrect PIN, please try again.")
                        verify_new_pin = int(input("Input your new PIN number again: \n"))
                        trial_new_pin+=1
                        if trial_new_pin==3 :
                            print("ATM BLOCKED!\nWe cannot process your transaction, please contact our customer service.")
                            exit()
                    while (verify_new_pin == update_pin) :
                        atm.newPin(verify_new_pin)
                        print("Yeay! Your PIN number changed successfully.")
                        break
                    next_transaction_menu_4_1 = int(input("Do you want to do another transaction? \n1. YES \t2. NO \n"))
                    if next_transaction_menu_4_1==1 :
                        choosing_menu
                    else :
                        print("Please take your ATM Card")
                        exit() 
                    break
                break
        elif choosing_menu==5 : #Exit and Receipt
            print("                 IMC Bank                ")
            print("         Your Transaction Record         ")
            print("-----------------------------------------")
            print(f"Record Number : {random.randint(100000,999999)}")
            print(f"Date          : {datetime.datetime.now()}")
            print(f"Balance       : {atm.checkBalance()}")
            print("-----------------------------------------")
            print("Receipt will be printed at the end of your transaction")

            exit()
        else:
            print("This service is not available")
            exit()
        #Intan Cahyaning