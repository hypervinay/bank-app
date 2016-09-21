def start_menu():
    print("Welcome to the atm!")
    if log_in():
    	print('Welcome to Northen Frock Bank ATM')
    	
def verify_pin(pin):
    if pin == 1234:
        return True
    else:
        return False

def log_in():
    tries = 0
    while tries < 4:
        pin = input('Please Enter Your 4 Digit Pin: ')
        if verify_pin(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            tries += 1
    print("To many incorrect tries. Could not log in")
    exit()
    

start_menu()
restart=('Y','y')
chances = 3
balance = 80.00
while chances >= 0:
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 To Make a Withdrawl\n')
            print('Please Press 3 To Pay in\n')
            print('Please Press 4 To Return Card\n')
            option = int(input('What Would you like to choose?'))
            if option == 1:
                print('Your Balance is',balance,'\n')
                restart = input('Would You like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would you like to withdraw? \n, for other enter 1: '))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print ('\nYour Balance is now',balance)
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount:'))    

            elif option == 3:
                Pay_in = float(input('How Much Would You Like To Pay In? '))
                balance = balance + Pay_in
                print ('\nYour Balance is now',balance)
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for you service')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
    
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break
print("Exiting Program")f
